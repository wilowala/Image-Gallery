from django.test import TestCase
from .models import Image,Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.bunny = Category(category_name='bunny')
        
    # Testing  instance to confirm that the object is being instantiated correctly.
    def test_instance(self):
        self.assertTrue(isinstance(self.bunny,Category))
    # Test saving
    def test_save_method(self):
        self.bunny.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)
        
class LocationTestClass(TestCase):
    def setUp(self):
        self.tanzania = Location(location_name='Tanzania')
        self.tanzania.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.tanzania, Location))

    def test_save_location(self):
        self.tanzania.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.tanzania.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
        
class TestImage(TestCase):
    def setUp(self):
       
        self.location = Location(location_name='Tanzania')
        self.location.save_location()
        self.category = Category(category_name='Animals')
        self.category.save_category()
        self.image_test = Image(id=1, img_name='kangaroo',img_description=' test image', location=self.location, category=self.category, posted_on ='2022-05-28')
        

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        after = Image.objects.all()
        self.assertTrue(len(after) > 0)
        
    def test_update_image(self):
        self.image_test.save_image()
        self.image_test.update_image(self.image_test.id, 'images/testimage.png')
        changed_image = Image.objects.filter(image='images/testimage.png')
        self.assertTrue(len(changed_image) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0) 
    
    def test_search_image_by_category(self):
        category = 'Animal'
        searched_images = self.image_test.search_image_by_cat(category)
        self.assertTrue(len(searched_images) < 1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()