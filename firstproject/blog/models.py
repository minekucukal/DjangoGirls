from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	yazar = models.ForeignKey('auth.User')
	baslik = models.CharField(max_length=200)
	yazi = models.TextField()
	olusturulmaTarihi = models.DateTimeField(default=timezone.now)
	yayinlamaTarihi = models.DateTimeField(
		blank=True, null=True)
	
	def yayinla(self):
		self.yayinlamaTarihi = timezone.now()
		self.save()

	def __str__(self):
		return self.baslik