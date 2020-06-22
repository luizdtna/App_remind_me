from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

    def show_all_tags(self):
        #return every register in DB
        return self.objects.all()

class Item(models.Model):
    name = models.CharField(max_length=20)
    place = models.TextField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='item_photos', null=True, blank=True)

    def show_datas(self):
        return self.objects.all()

    def show_data_by_id(self,id):
        pass
        #return self.get_object_or_404(self, pk=id)

    def filter_by_tag(self,tagName):
        item = Item.objects.filter(tag__name=tagName)

    def __str__(self):
        return self.name


