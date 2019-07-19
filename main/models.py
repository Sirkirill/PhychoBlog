"""
Stores all models of the project
"""
from django.contrib.auth.models import User
from django.db import models

from psycho.settings import st_password


class PhotoItem(models.Model):
    """
    Abstract
    help to store information about the photo
    """
    id = models.AutoField(primary_key=True)
    photo = models.ImageField('Изображение', height_field='height', width_field='width', null=True, blank=True)
    alt = models.TextField("Описание фото", max_length=200, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        """
        PhotoItem model settings
        """
        abstract = True
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'


class Person(PhotoItem):
    """
    Stores all information about a psychologist
    """
    id = models.AutoField(primary_key=True)
    full_name = models.CharField('Полное имя', max_length=50)
    name = models.CharField('Логин', max_length=20, unique=True)
    birth_date = models.DateField('Дата рождения')
    email = models.EmailField()
    info = models.TextField('Основная информация', blank=True)
    bio = models.TextField('Биография', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.user:
            user = User.objects.get(id=self.user.id)
            user.username, user.email = self.name, self.email
            user.save()
        else:
            user = User.objects.create_user(self.name, self.email, st_password)
            user.save()
            self.user = user
            user.groups.add(1)
            user.is_staff = True
            user.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        user = User.objects.get(id=self.user.id)
        print(1)
        if not user.is_superuser:
            user.delete()
            super().delete(*args, **kwargs)
        else:
            print("superuser can't be deleted")
            print(user.id)

    def __str__(self):
        return self.full_name

    class Meta:
        """
        Person model settings
        """
        db_table = 'people'
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


EventType = (
    ('common', 'Обучение для всех'),
    ('prof', 'Обучение для профессионалов'),
    ('personal', 'Программы личностного роста'),
    ('university', 'Базовое психологическое образование в хгак'),
)


class Event(PhotoItem):
    """
    Stores information about a single event
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    content = models.TextField("Контент", max_length=200, blank=True, null=True)
    start_date = models.DateTimeField('Дата начала мероприятия')
    duration = models.CharField('Длительность', max_length=20, blank=True, null=True)
    type = models.CharField(max_length=20, choices=EventType, default='common')

    def __str__(self):
        return self.name

    class Meta:
        """
        Event model settings
        """
        db_table = 'events'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Article(models.Model):
    """
    Stores a single article entry
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    content = models.TextField("Контент", blank=True)
    content_min = models.TextField("Миниверсия статьи", max_length=300, blank=True)
    release_date = models.DateTimeField("Дата выпуска статьи", auto_now_add=True)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        """
        Article model settings
        """
        db_table = 'articles'
        ordering = ['release_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Announcement(models.Model):
    """
    Stores am announcement entry
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    content = models.TextField("Контент", max_length=200, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Мероприятие")
    main = models.BooleanField("Отображать вверху", default=False)

    def __str__(self):
        return self.name

    class Meta:
        """
        Announcement model settings
        """
        db_table = 'announcements'
        ordering = ['-main', 'event__start_date']
        verbose_name = 'Анонс'
        verbose_name_plural = 'Анонсы'


class HelpItem(models.Model):
    """
    Stores information about the type of help
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField("Название", max_length=50)
    description = models.TextField("Описание", null=True, blank=True, max_length=200)
    expert = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Эксперт')

    def __str__(self):
        return self.name

    class Meta:
        """
        HelpItem model settings
        """
        db_table = 'help'
        verbose_name = 'Пункт помощи'
        verbose_name_plural = 'Пункты помощи'


class Achievement(PhotoItem):
    """
    Stores information about a single certificate or other proof of competence
    """
    priority = models.IntegerField("Приоритет", default=2)
    expert = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Эксперт')

    def __str__(self):
        return self.alt

    class Meta:
        """
        Achievement model settings
        """
        db_table = 'achievements'
        verbose_name = 'Достижение'
        ordering = ['-priority']
        verbose_name_plural = 'Достижения'


class ArticlePhotoReport(PhotoItem):
    """
    Stores photos for articles
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Статья")

    def __str__(self):
        return self.alt

    class Meta:
        """
        ArticlePhotoReport model settings
        """
        db_table = 'photos'
        verbose_name = 'Фото для статьи'
        verbose_name_plural = 'Фото для статьи'
