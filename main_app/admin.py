from django.contrib import admin

# import your models here.
from .models import Toad, Feeding, Toy

# Register your models here
admin.site.register(Toad)
admin.site.register(Feeding)
admin.site.register(Toy)
