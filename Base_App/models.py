from django.db import models

# Create your models here.
class ItemList(models.Model):
    Category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.Category_name

class Items(models.Model):
    Item_name = models.CharField(max_length=200)
    Description = models.TextField(blank=False)
    price = models.IntegerField(null=True)
    Caregory = models.ForeignKey(ItemList, related_name='items_categories', on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='Items/')
    
    def __str__(self):
        return self.Item_name

class AboutUs(models.Model):
    Description = models.TextField(blank=False)

class Feedback(models.Model):
    User_name = models.CharField(max_length=200)
    Description = models.TextField(blank=False)
    Ratting = models.IntegerField()
    Image = models.ImageField(upload_to='Items/',blank=True)
    
    def __str__(self):
        return self.User_name

class BookTable(models.Model):
    Name = models.CharField(max_length=200)
    Phone_number = models.CharField(max_length=200)
    Email = models.EmailField()
    Total_person = models.IntegerField()
    Booking_date = models.DateField()
    
    def __str__(self):
        return self.Name