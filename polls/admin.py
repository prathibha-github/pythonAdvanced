from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    list_display = ['pk','question','pub_date','was_published_recently']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['pk','choice_text', 'votes']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)