from django.db import models

# Create your models here.
class Helmet(models.Model):
   helmet_id = models.AutoField(auto_created=True, primary_key=True)
   model = models.CharField(max_length=10)
   price = models.CharField(max_length=10)
   image = models.FileField(upload_to="images/helmet/")

   class Meta:
       db_table = "helmet"
