from wagtailmodeladmin.options import ModelAdmin, wagtailmodeladmin_register
from .models import Message


class MessageAdmin(ModelAdmin):
    model = Message
    menu_label = 'Messages'
    menu_icon = 'date'
    menu_order = 200
    add_to_settings_menu = False
    list_display = ('contact_date', 'contacted', 'sender', 'email', 'number', 'category', 'message')
    list_filter = ('contacted', 'category', 'contact_date')
    search_fields = ('sender', 'email', 'body',)

wagtailmodeladmin_register(MessageAdmin)
