# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Text(models.Model):
    DEFAULT = 'DF'
    emotion = 'EM'
    diary = 'DI'
    article = 'AR'
    soso = 'SO'

    INFOTYPE_CHOICES = (
            (emotion, '感性文章'),
            (diary, '松鼠日记'),
            (article, '奇文共赏'),
            (soso, '随便溜溜'),
            (DEFAULT, '未分类地'),
    )
    title = models.CharField(max_length = 32)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True, blank = True)
    infotype = models.CharField(max_length = 3, 
                                choices = INFOTYPE_CHOICES,
                                default = DEFAULT) 
    tag = models.CharField(max_length = 32)
    abstract = models.CharField(max_length = 100)
    reward = models.CharField(max_length = 32)
    noreward = models.CharField(max_length = 32)


