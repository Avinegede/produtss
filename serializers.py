from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
   
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)
    doc = serializers.FileField(max_length=None, use_url=True)
   
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['id', 'Producer','posted_by', 'productName', 'productType','description', 'amount', 'price','discount']
       