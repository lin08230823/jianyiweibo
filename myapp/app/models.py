from django.db import models
from django.contrib.auth.admin import User
import json
import datetime
# Create your models here.

class WBUser(User):

    GENDER_OPTIONS = (
        (0,'保密'),
        (1,'男'),
        (2,'女'),
        (3,'其他')
    )
    nickname = models.CharField(verbose_name='昵称',max_length=60,unique=True,blank=True,null=True)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_OPTIONS, default=0)
    _info = models.TextField(verbose_name='其他',blank=True,null=True)
    followers = models.ManyToManyField(to='WBUser')

    @property
    def name(self):
        return self.nickname or self.username

    @property
    def info(self):
        return json.loads(self._info)

    def save_user_info(self, info: dict):
        self._info = json.dumps(info)
        self.save()


    def update(self, msg: str):
        wbt = WBText.objects.create(author=self, msg=msg )
        wb = WeiBo.objects.create(user=self, text=wbt)
        return wb

    def follow(self, user:'WBUser'):

        self.followers.add(user)

    def unfollow(self, user: 'WBUser'):

        self.followers.remove(user)

    def forward(self, wb: 'WeiBo'):
        return WeiBo.objects.create(user=self, text=wb.text)


    def __str__(self):
        return self.name

class WBText(models.Model):
    author = models.ForeignKey(WBUser, verbose_name='作者',on_delete=models.CASCADE)
    msg = models.TextField(verbose_name='微博', max_length=500)
    def __str__(self):
        return '{msg}...'.format(msg=self.msg[:20])

class WeiBo(models.Model):
    user = models.ForeignKey(WBUser,verbose_name='用户', related_name='weibos',on_delete=models.CASCADE)
    time_create = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_del = models.BooleanField(verbose_name='是否删除', default=False)
    text = models.ForeignKey(WBText,verbose_name='文本', related_name='weibos',on_delete=models.CASCADE)

    def del_this(self):
        self.is_del = True
        self.save()
    def comment_this(self, user:WBUser,text:str):
        comment = Comment.objects.create(user=user, text=text, target=self)
        return comment
    def __str__(self):
        return self.text.__str__()


class Comment(models.Model):
    target = models.ForeignKey(WeiBo,verbose_name='微博',related_name='comments',on_delete=models.CASCADE)
    user = models.ForeignKey(WBUser,verbose_name='用户', related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(verbose_name='评论内容', max_length=500)
    time_create = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    is_del = models.BooleanField(verbose_name='是否删除',default=False)

    def del_this(self):
        self.is_del = True
        self.save()

    def __str__(self):
        return'{msg}...'.format(msg=self.text[:20])