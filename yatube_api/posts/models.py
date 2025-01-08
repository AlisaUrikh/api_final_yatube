from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    """Модель групп."""

    title = models.CharField(max_length=200, verbose_name='Название группы')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title


class Post(models.Model):
    """Модель публикаций."""

    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
                                    auto_now_add=True,
                                    verbose_name='Дата публикации')
    author = models.ForeignKey(
                               User, on_delete=models.CASCADE,
                               related_name='posts',
                               verbose_name='Автор поста',)
    image = models.ImageField(
                              upload_to='posts/',
                              null=True,
                              blank=True,
                              verbose_name='Изображение')
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Идентификатор группы')

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Модель комментариев."""

    author = models.ForeignKey(
                               User,
                               on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='Автор комментария')
    post = models.ForeignKey(
                             Post,
                             on_delete=models.CASCADE,
                             related_name='comments',
                             verbose_name='Пост')
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
                                   auto_now_add=True,
                                   db_index=True,
                                   verbose_name='Дата добавления')

    def __str__(self):
        return (f'Комментарий {self.author} к "{self.post}": '
                f'{self.text}')


class Follow(models.Model):
    """Модель подписчиков и подписок."""

    user = models.ForeignKey(
                             User, on_delete=models.CASCADE,
                             related_name='follower',
                             verbose_name='Пользователь-подписчик')
    following = models.ForeignKey(
                                  User,
                                  on_delete=models.CASCADE,
                                  related_name='following',
                                  verbose_name='Пользователь-подписка')

    def __str__(self):
        return (f'Пользователь {self.user} '
                f'подписался на {self.following}')
