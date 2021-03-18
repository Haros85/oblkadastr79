from django.contrib import admin

from .models import News, Glossary, Act


class NewsAdmin(admin.ModelAdmin):
    list_display = ("pk", "pub_date", "title")
    search_fields = ("title",)
    list_filter = ("pub_date",)


class GlossaryAdmin(admin.ModelAdmin):
    list_display = ("pk", "title")
    search_fields = ("title",)
    list_filter = ("title",)


class ActAdmin(admin.ModelAdmin):
    list_display = (
        "number",
        "pub_date",
        "num_obj",
        "type_act",
        "path",
    )
    search_fields = ("number",)
    list_filter = ("type_act",)


admin.site.register(News, NewsAdmin)
admin.site.register(Glossary, GlossaryAdmin)
admin.site.register(Act, ActAdmin)
