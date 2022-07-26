from django.db import models

# Create your models here.
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from timestamps.models import Model

class Producer(Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Product (models.Model) :
    Producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/', default='Images/None/No-img.jpg') 
    doc = models.FileField(upload_to='Doc/',default='Doc/None/No-doc.pdf')
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    productName = models.CharField(max_length=100)
    productType = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    amount = models.PositiveIntegerField(_("Amount"))
    price = models.DecimalField(_("Price"), max_digits=6, decimal_places=2)
    discount = models.DecimalField(_("Discount"), max_digits=3, decimal_places=2, blank=True, null=True)



    def __str__(self):
        return self.posted_by