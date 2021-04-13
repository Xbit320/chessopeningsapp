from django.db import models

# Create your models here.
class Categories(models.Model):
    category =models.CharField(max_length=200,primary_key=True)

    def __str__(self):
        return self.category

class CategoriesTypes(models.Model):
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    category_type =models.CharField(max_length=200,primary_key=True,default="Default")
    def __str__(self):
        return self.category_type

class Opening(models.Model):
    
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    category = models.ForeignKey(Categories,on_delete=models.CASCADE)
    category_type = models.ForeignKey(CategoriesTypes,on_delete=models.CASCADE)
    image = models.CharField(max_length=300)
    description = models.TextField(default="None")
    embed_code = models.TextField(default="None")
    embed_code_chess_com = models.TextField(default="None")