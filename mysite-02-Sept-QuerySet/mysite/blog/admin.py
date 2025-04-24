from django.contrib import admin

from .models import Blog, Author, Entry

class BlogAdmin(admin.ModelAdmin):


    list_display  = ['name','tagline']

admin.site.register(Blog,BlogAdmin)


class AuthorAdmin(admin.ModelAdmin):


    list_display  = ['name','email']

admin.site.register(Author,AuthorAdmin)


class EntryAdmin(admin.ModelAdmin):


    list_display  = ['blog','headline','body_text','pub_date','mod_date','number_of_comments','number_of_pingbacks']  

admin.site.register(Entry,EntryAdmin)





 #    Blog : ['name','tagline']

 #    Author : ['name','email']

 #    Entry : ['blog','headline','body_text','pub_date','mod_date',
 #    'authors','number_of_comments','number_of_pingbacks']    


	# class Admin(admin.ModelAdmin):


	#     list_display  = 

	# admin.site.register()
