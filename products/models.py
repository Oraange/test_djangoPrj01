from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    korean_name     = models.CharField(max_length=45)
    english_name    = models.CharField(max_length=45)
    description     = models.TextField()
    nutrition       = models.ForeignKey('Nutrition', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
        

    class Meta:
        db_table = 'products'

class Image(models.Model):
    image_url = models.CharField(max_length=200)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

class Nutrition(models.Model):
    one_sercving_kal = models.DecimalField(max_digits=5, decimal_places=2)
    sodium_mg = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat_g = models.DecimalField(max_digits=5, decimal_places=2)
    sugars_g = models.DecimalField(max_digits=5, decimal_places=2)
    protein_g = models.DecimalField(max_digits=5, decimal_places=2)
    caffeine_mg = models.DecimalField(max_digits=5, decimal_places=2)
    size_ml = models.CharField(max_length=45)
    size_fluid_ounce = models.CharField(max_length=45)

    class Meta:
        db_table = 'nutritions'

class Allergy(models.Model):
    name = models.CharField(max_length=45)
    product = models.ManyToManyField('Product', through = 'Allergy_product')

    class Meta:
        db_table = 'allergy'

class Allergy_product(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'allergy_products'
