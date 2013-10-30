from django.db import models
from django import forms
from django_extensions.db.fields import UUIDField
import uuid

class NGO(models.Model):
	name = models.CharField(max_length=50)
	website = models.URLField()
	logo = models.ImageField(upload_to="kdr/static/img/database_items/")

	def __unicode__(self):
		return self.name

class NGO_Classification(models.Model):
	CLASSIFICATIONS = (
		('Environmental', 'Environmental'),
		('Justice', 'Justice'),
		('International', 'International'),
		('Health', 'Health'),
		('Education', 'Education'),
		('Energy', 'Energy'),
	)
	classification = models.CharField(max_length=50, choices=CLASSIFICATIONS, default='Environmental')

	def __unicode__(self):
		return self.classification

class NGO_Post(models.Model):
	NEWS_MONTHS = (
		('January', 'A-January'),
		('February', 'B-February'),
		('March', 'C-March'),
		('April', 'D-April'),
		('May', 'E-May'),
		('June', 'F-June'),
		('July', 'G-July'),
		('August', 'H-August'),
		('September', 'I-September'),
		('October', 'J-October'),
		('November', 'K-November'),
		('December', 'L-December'),
	)
	
	title = models.CharField(max_length=50)
	month = models.CharField(max_length=15, choices=NEWS_MONTHS, default='January')
	year = models.IntegerField(max_length=4)
	news = models.TextField()
	author = models.CharField(max_length=30, blank=True)
	original_link = models.URLField()
	ngo = models.ForeignKey(NGO)
	image = models.FileField(upload_to="static/img/database_items/")
	classifications = models.ManyToManyField(NGO_Classification)
	post_id = UUIDField()

	def __unicode__(self):
		return self.title

	class Meta:
		ordering = ('title', )

	

	
