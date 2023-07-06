from django.contrib import admin
from .models import AddItem, Journal,Purchase,Sales,Unit

# Register your models here.
admin.site.register(AddItem)
admin.site.register(Purchase)
admin.site.register(Sales)
admin.site.register(Unit)
@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_display = ('journal_no', 'date', 'status')
    actions = ['publish_journals']

    def publish_journals(self, request, queryset):
        queryset.update(status='published')
        self.message_user(request, 'Selected journals have been published.')
    publish_journals.short_description = 'Publish selected journals'