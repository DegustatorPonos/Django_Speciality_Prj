from django.db import models

# Create your models here.

class Paragraph(models.Model):
	targetpage = models.CharField('Trg', max_length=50)
	subtitle = models.CharField('Subtitle', max_length=50)
	value = models.TextField('Content')

	def __str__(self):
		return self.subtitle