from django.db import models

# Create your models here.
#


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)
    image=models.ImageField(upload_to='product/image123')
    prise=models.FloatField(max_length=5000)

    def __str__(self):
        return self.title


class order(models.Model):
    ordered_items=models.ForeignKey(Product,on_delete=models.CASCADE)   
    total_prise=models.FloatField(verbose_name='summa')  
    creatid_alt=models.DateField(auto_now=True)
    phone=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.phone
