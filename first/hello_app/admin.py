from django.contrib import admin
from hello_app.models import Topic,Webpage,AcessRecord

# Register your models here.
admin.site.register(AcessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
