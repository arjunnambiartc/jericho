from django.contrib import admin, messages
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, ModelForm, Textarea, Select
from reversion import VersionAdmin
from import_export.admin import ImportExportModelAdmin
from suit_ckeditor.widgets import CKEditorWidget
from suit_redactor.widgets import RedactorWidget
from .models import Year,Weekend,Change
from suit.admin import SortableTabularInline, SortableModelAdmin
from suit.widgets import SuitDateWidget, SuitSplitDateTimeWidget, EnclosedInput, LinkedSelect, AutosizedTextarea
from django_select2 import AutoModelSelect2Field, AutoHeavySelect2Widget
from mptt.admin import MPTTModelAdmin


class ChangeForm(ModelForm):
    class Meta:
        widgets = {
            'Start_Time': SuitSplitDateTimeWidget,
            'End_Time': SuitSplitDateTimeWidget,
            'User_Requested_Time': SuitSplitDateTimeWidget,
            'Description': AutosizedTextarea(attrs={'class': 'span5'}),
        }


class ChangeAdmin(ModelAdmin):
    form = ChangeForm
    search_fields = ('RFC', 'Ticket_Number', 'User_Email', 'Change_Details')
    list_display = ('RFC', 'Ticket_Number', 'Start_Time', 'End_Time')
    date_hierarchy = 'Start_Time'
    list_select_related = True

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['RFC', 'Ticket_Number']}),
        ('Timelines', {
            'classes': ('suit-tab suit-tab-general',),
            'description': 'All associated Time lines ',
            'fields': ['Start_Time', 'End_Time', 'User_Requested_Time']}),
                ]

    suit_form_tabs = (('plan', 'Plan'))

admin.site.register(Change, ChangeAdmin)