from django.db import models
from helmet.models import Helmet
from customer.models import Customer
# Create your models here.
class Order(models.Model):
    Order_id = models.AutoField(auto_created=True, primary_key=True)
    helmet=models.ForeignKey(Helmet,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    class Meta:
        db_table = "order"
