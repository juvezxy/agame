from django.contrib import admin

# Register your models here.
from .models import Segment, Question

class SegmentInline(admin.TabularInline):
    model = Segment
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [SegmentInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']
    list_display = ('question_text', 'pub_date')

admin.site.register(Question, QuestionAdmin)