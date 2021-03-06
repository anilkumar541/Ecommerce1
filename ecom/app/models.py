from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

state_choices = (("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),("Bihar","Bihar"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Chandigarh","Chandigarh")

)

category_choices=(
    ("M", "Mobile"),
    ("L", "Laptop"),
    ("TW", "Top Wear"),
    ("BW", "Bottom Wear"),
)

status_choices=(
    ("Accepted", "Accepted"),
    ("Packed", "Packed"),
    ("On The Way", "On The Way"),
    ("Delivered", "Delivered"),
    ("Cancel", "Cancel"),
)

class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    zipcode=models.IntegerField()
    state=models.CharField(choices=state_choices, max_length=100)

    class Meta:
        db_table="customers"    

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    brand=models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(choices=category_choices, max_length=30)
    product_image=models.ImageField(upload_to="productImages")

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table="products" 

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table="cart"

    @property   
    def total_cost(self):
        return self.quantity*self.product.discounted_price


class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(choices=status_choices, max_length=50, default="pending")

    def __str__(self):
        return str(self.id)
    class Meta:
        db_table="order_placed"
    @property   
    def total_cost(self):
        return self.quantity*self.product.discounted_price    



