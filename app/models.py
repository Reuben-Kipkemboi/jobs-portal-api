from django.utils.text import slugify
from django.db import models
import datetime as dt
from django.contrib.auth.models import User


# jobs category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=200, default='fa fa-briefcase')
    description = models.TextField(max_length=300, default='')

    def __str__(self):
        return self.name


# jobs model
class Job(models.Model):
    company_name = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=100)
    company_phone = models.CharField(max_length=100)
    company_website = models.CharField(max_length=1000, default='')
    company_linkedin = models.CharField(max_length=1000, default='')
    company_logo = models.TextField(null=True, blank=True)
    company_location = models.CharField(max_length=300)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, default='')
    salary_range = models.CharField(max_length=100, default='')
    job_type = models.CharField(max_length=100, default='Full Time')
    job_description = models.TextField(max_length=5000, default='')
    location = models.CharField(max_length=100, default='')
    application_deadline = models.DateTimeField()
    experience = models.IntegerField(default=0)
    qualification = models.CharField(max_length=100, default='')
    link_to_job = models.CharField(max_length=1000, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    # order by created_at descending
    class Meta:
        ordering = ['-created_at']
