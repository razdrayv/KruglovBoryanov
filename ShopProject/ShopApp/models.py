from django.db import models


class Category(models.Model):
    nameCategory = models.CharField('Категория',max_length=50)

    def __str__(self):
        return self.nameCategory
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

#сделать названия полей и добавить ко всем моделям класс мета и verbose name
class Product(models.Model):
    title = models.CharField('Название',max_length=100)
    price = models.IntegerField('Цена',)
    made = models.CharField('Производитель',max_length=100)
    image = models.FileField('Картинка',upload_to='img/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'