from django.db import models

# Create your models here.
class Destinations(models.Model):
	dest_id=models.IntegerField(primary_key=True)
	dest_name=models.CharField(max_length=15,default="")
	class Meta:
		verbose_name_plural="dest"

class Basic_Itineraries(models.Model):
	it_id=models.IntegerField(primary_key=True)
	no_days=models.IntegerField(default=0)
	total_kms=models.IntegerField(default=0)
	it_desc=models.CharField(max_length = 256)

	class Meta:
		verbose_name_plural="iti"

class basic_dest_ids(models.Model):
	b_id=models.IntegerField(primary_key=True,default=0)
	it_id=models.ForeignKey(Basic_Itineraries,default=0,on_delete=models.SET_DEFAULT,verbose_name="dest")
	dest_id=models.ForeignKey(Destinations,default=0,on_delete=models.SET_DEFAULT,verbose_name="iti")
