from django.contrib import admin
from poll.models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    """allow coices to be accessed in Question page"""
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """changing render of admin for Question"""
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields':['pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

