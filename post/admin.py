from django.contrib import admin

from .models import PostModel

class PostAdmin(admin.ModelAdmin):
    list_display=['title','description','date']
    list_display_links=['title']
    readonly_fields = ['date']
    #list_editable = ['description']
    search_fields = ['title']
    list_filter = ['date','title']
    fieldsets = (
      (
         'Main part',{
           'fields':('title',)
      }

    ),
       (
          'Second part', {
          'fields': ('description','date')
      }

      )
    )

# Register your models here.
admin.site.register(PostModel,PostAdmin)


