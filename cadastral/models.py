from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", db_index=True)
    image = models.ImageField(upload_to="news/", blank=True, null=True)

    class Meta:
        verbose_name = u"Новость"
        verbose_name_plural = u"Новости"
        ordering = ["-pub_date"]

    def __str__(self):
        return self.title

class Glossary(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    doc = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = u"Глоссарий"
        verbose_name_plural = u"Глоссарий"
        ordering = ["pk"]

    def __str__(self):
        return self.title

class Act(models.Model):
    TYPE_ACTS = (
        ("act", "Акт"),
        ("report", "Отчёт"),
    )
    number = models.CharField(max_length=20)
    pub_date = models.DateField()
    num_obj = models.PositiveIntegerField()
    type_act = models.CharField(max_length=6, choices=TYPE_ACTS)
    path = models.FileField(upload_to="files/acts/")

    class Meta:
        verbose_name = u"Акт/Отчёт"
        verbose_name_plural = u"Отчёты и акты"
        ordering = ["-pub_date","-number"]

    def __str__(self):
        return self.number

