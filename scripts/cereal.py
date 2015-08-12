#!/usr/bin/env python
import csv
import os
import sys

sys.path.append("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()


from main.models import Manufacturer, Cereal, Nutrition_Facts


csv_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , 'cereal.csv')

csv_file = open(csv_file_path, 'r')

reader = csv.DictReader(csv_file)

for row in reader:
	print row['Cereal Name'].replace('_', ' ')
	print row['Manufacturer']

	manu_obj, created = Manufacturer.objects.get_or_create(name=row['Manufacturer'])

	cereal_obj, created = Cereal.objects.get_or_create(name=row['Cereal Name'])
	cereal_obj.manufacturer = manu_obj
	cereal_obj.display_shelf = row['Display Shelf']
	cereal_obj.type=row['Type']
	cereal_obj.save()

	nut_facts, created = Nutrition_Facts.objects.get_or_create(calories=row['Calories'],
																protein=row['Protein (g)'],
																fat=row['Fat'],
																sodium=row['Sodium'],
																dietary_fiber=row['Dietary Fiber'],
																carbs=row['Carbs'],
																sugars=row['Sugars'],
																potassium=row['Potassium'],
																vitamins_and_minirals=row['Vitamins and Minerals'],
																serving_size_weight=row['Serving Size Weight'],
																cups_per_serving=row['Cups per Serving'],
																cereal=cereal_obj)


	# print manu_obj.name
	# print created

	# print row['Type']
	# print row['Calories']
	# print row['Protein (g)']
	# print row['Fat']
	# print row['Sodium']
	# print row['Dietary Fiber']
	# print row['Carbs']
	# print row['Sugars']
	# print row['Display Shelf']
	# print row['Potassium']
	# print row['Vitamins and Minerals']
	# print row['Serving Size Weight']
	# print row['Cups per Serving']

#csv_file_path2 = "%s/cereal.csv" % (os.path.dirname(os.path.abspath(__file__)))

# print os.path.abspath(__file__)

# print os.path.dirname(os.path.abspath(__file__))

# print csv_file_path

# print csv_file_path2
