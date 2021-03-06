from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import  pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.

class Publisher(models.Manager):
    def get_queryset(self):
        return super(Publisher, self).get_queryset().filter(status='published')

class Drafted(models.Manager):
    def get_queryset(self):
        return super(Drafted, self).get_queryset().filter(status='draft')

class News(models.Manager):
    def get_queryset(self):
        return super(News, self).get_queryset().filter(category='news')

class Entertainment(models.Manager):
    def get_queryset(self):
        return super(Entertainment, self).get_queryset().filter(category='entertainment')

class Technology(models.Manager):
    def get_queryset(self):
        return super(Technology, self).get_queryset().filter(category='tech')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('featured', 'Featured'),
    )

    CATEGORY_CHOICES = (
        ('entertainment', 'Entertainment'),
        ('news', 'News'),
        ('tech', 'Technology'),
    )
    title = models.CharField(max_length=100)
    cover_photo = models.ImageField(upload_to='images/', blank=False, null=False, default='images/download.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=120)
    body = models.TextField(editable=True)
    author = models.ForeignKey(User, related_name='article_posts', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='entertainment')
    objects = models.Manager()
    likes =  models.ManyToManyField(User, related_name='likes', blank=True)
    published = Publisher() #Custom model manager.
    drafted = Drafted()
    news = News()
    entertainment = Entertainment()
    tech = Technology()
    restrict_comments = models.BooleanField(default=False)
    favourites = models.ManyToManyField(User, related_name='favourites', blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + "..."

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.id, "slug": self.slug})

    def total_likes(self):
        return self.likes.count

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    kwargs['instance'].slug = slugify(kwargs['instance'].title)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/', default="default.png")

    def __str__(self):
        return "Profile of user {}".format(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()








class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)



    def __str__(self):
        return self.post.title + ' image'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply = models.ForeignKey('self', null=True, related_name='replies', on_delete=models.CASCADE)
    content = models.TextField(max_length=180)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.post.title, str(self.user.username))