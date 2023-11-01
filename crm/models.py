from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    image=models.ImageField(upload_to="images",null=True)
    options={
        ("male","male"),
        ("female","female"),
        ("other","other")
    }
    gender=models.CharField(max_length=200,choices=options,default="male")

    def _str_(self):
        return self.name