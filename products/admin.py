from django.contrib import admin
from .models import Chair, Feature


class ChairAdmin(admin.ModelAdmin):
    list_display = ('model_number', 'model_image')


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature_image', 'chair')


admin.site.register(Chair, ChairAdmin)
admin.site.register(Feature, FeatureAdmin)

