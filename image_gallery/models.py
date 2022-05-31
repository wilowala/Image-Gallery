from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.location_name
          
    def save_location(self):
        self.save() 
        
    def delete_location(self):
        self.delete()       
   
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save() 
        
    def delete_category(self):
        self.delete()
        
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    img_name = models.CharField(max_length=110)
    img_description = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.img_name
    class  Meta:
        ordering=['posted_on']

    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
    
    @classmethod
    def update_image(cls,img_id, item):
        cls.objects.filter(id=img_id).update(image=item)
        
    @classmethod
    def get_image_byid(cls,id):
        image = cls.objects.filter(id=id).all()
        return image
    
    @classmethod
    def get_images(cls):
        image = cls.objects.all()
        return image
    
    @classmethod
    def search_image_by_cat(cls,category_name):
        res_images = cls.objects.filter(category=Category.objects.filter(category_name__icontains=category_name).first()).all()
        return  res_images

    @classmethod
    def filter_by_location(cls,locat):
        res_images = cls.objects.filter(location_icontains=locat) 
        return res_images