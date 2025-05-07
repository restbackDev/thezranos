from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Food(models.Model):
  name = models.CharField(max_length=20)
  grams = models.IntegerField()
  calories = models.IntegerField()

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('food-detail', kwargs={'pk': self.id})


class Date(models.Model):
  day = models.DateField(null=False, blank=False)
  weight= models.IntegerField()
  water_intake = models.IntegerField()
  # Add the M:M relationship
  foods = models.ManyToManyField(Food)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def get_absolute_url(self):
    # Use the 'reverse' function to dynamically find the URL for viewing this date's details
    return reverse('date-detail', kwargs={'date_id': self.id})
  
  # convert pounds(lbs) --> kilograms(kg) --> grams per kilograms of protein(g)
  def protein_per_weight(self):
    weight= self.weight * 0.453592  # lbs --> kg
    protein_grams = weight * 0.8 # kg --> g (per protein)
    return int(protein_grams) 

  def total_protein(self):
    total = 0
    for food_grams in self.foods.all():
      total += food_grams.grams
      return total
    
    
  # def __str__(self):
  #   return self.day



