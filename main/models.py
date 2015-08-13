from django.db import models

# Create your models here.

class Manufacturer(models.Model):
	name = models.CharField(max_length=255,unique=True)

	def __unicode__(self):
		return self.name

class Cereal(models.Model):
	name = models.CharField(max_length=255,null=True)
	manufacturer = models.ForeignKey('main.Manufacturer',null=True)
	type = models.CharField(max_length=255,null=True)
	display_shelf = models.IntegerField(null=True)
	image = models.ImageField(upload_to="cereal", null=True)
	info = models.TextField()
	#nutrition_facts = models.OneToOneField('main.Nutrition_Facts',null=True)
	
	def __unicode__(self):
		return self.name



class Nutrition_Facts(models.Model):
	calories = models.IntegerField(null=True)
	protein = models.IntegerField(null=True)
	fat = models.IntegerField(null=True)
	sodium = models.FloatField(null=True)
	dietary_fiber = models.FloatField(null=True)
	carbs = models.FloatField(null=True)
	sugars = models.IntegerField(null=True)
	potassium = models.IntegerField(null=True)
	vitamins_and_minirals = models.IntegerField(null=True)
	serving_size_weight = models.FloatField(null=True)
	cups_per_serving = models.FloatField(null=True)
	cereal = models.OneToOneField('main.Cereal',null=True)
	#cereal = models.ForeignKey('main.Cereal',null=True)

	def __unicode__(self):
		return self.cereal.nameca

	def nutrition_list(self):
		value_list = []
		value_list.append("calories: %s" % self.calories)
		value_list.append("protein: %s" % self.protein)
		value_list.append("fat: %s" % self.fat)
		value_list.append("sodium: %s" % self.sodium)
		value_list.append("dietary_fiber: %s" % self.dietary_fiber)
		value_list.append("carbs: %s" % self.carbs)
		value_list.append("sugars: %s" % self.sugars)
		value_list.append("potassium: %s" % self.potassium)
		value_list.append("vitamins_and_minirals: %s" % self.vitamins_and_minirals)
		value_list.append("serving_size_weight: %s" % self.serving_size_weight)
		value_list.append("cups_per_serving: %s" % self.cups_per_serving)

		return value_list




