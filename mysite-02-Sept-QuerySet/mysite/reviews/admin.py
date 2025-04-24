from django.contrib import admin

from reviews.models import comments


class commentsAdmin(admin.ModelAdmin):

    list_display  = ['name','description']

admin.site.register(comments,commentsAdmin)



# comments : ['blog','description']

# Register your models here.
