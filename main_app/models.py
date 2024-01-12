from django.db import models
from django.urls import reverse
from datetime import date

# Create your models here.

SIGHT = (
    ('E', 'Early Morning'),
    ('M', 'Midday'),
    ('L', 'Late Afternoon')
)

class Toy(models.Model):
    name= models.CharField(max_length=100)
    color= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})


class Finch(models.Model):
    name = models.CharField(max_length=100)
    distribution = models.CharField(max_length=100)
    habitat = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})
    
    def seen_for_today(self):
        return self.sighting_set.filter(date=date.today()).count() >= len(SIGHT)

class Sighting(models.Model):
    date = models.DateField('Sighting Date')
    time = models.CharField(
        max_length=1,
        choices = SIGHT,
        default = SIGHT[0][0]
     )
    
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    


    def __str__(self):
        return f"{self.get_sight_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
        return f"Photo for finch_id: {self.finch_id} @{self.url}"