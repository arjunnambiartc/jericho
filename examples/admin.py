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
from guardian.admin import GuardedModelAdmin


class ChangeForm(ModelForm):
    class Meta:
        widgets = {
            'Start_Time': SuitSplitDateTimeWidget,
            'End_Time': SuitSplitDateTimeWidget,
            'User_Requested_Time': SuitSplitDateTimeWidget,
            'Conf_Call_Details': AutosizedTextarea(attrs={'class': 'span5'}),
            'Configuration_Item': AutosizedTextarea(attrs={'class': 'span4'}),
            'Change_Details': TextInput(attrs={'class': 'span6'}),
            'Summary': AutosizedTextarea(attrs={'class': 'span6'}),
            'Description': AutosizedTextarea(attrs={'class': 'span6'}),
            'Comments': AutosizedTextarea(attrs={'class': 'span5'}),
        }


class ChangeAdmin(GuardedModelAdmin):
    form = ChangeForm
    search_fields = ('RFC', 'Ticket_Number', 'User_Email', 'Change_Details')
    list_display = ('RFC', 'Ticket_Number', 'User_Requested_Time', 'Start_Time', 'End_Time',
                    'User_Email', 'Line_of_Business', 'Conf_Call_Details', 'Region',
                    'Summary', 'Description', 'Change_Details', 'Site_code', 'Configuration_Item',
                    'Plan_Owner', 'Plan_status', 'Change_Owner', 'Implementer', 'Validator')
    date_hierarchy = 'Start_Time'
    list_select_related = True

    fieldsets = [
        ('Ticket Details', {
            #'classes': ('suit-tab suit-tab-general',),
            'fields': ['RFC', 'Ticket_Number']}),
        ('Timelines', {
            #'classes': ('suit-tab suit-tab-general',),
            'description': 'All associated Time lines ',
            'fields': ['Start_Time', 'End_Time', 'User_Requested_Time']}),
        ('User Details', {
            'fields': ['User_Email', 'Line_of_Business', 'Conf_Call_Details', 'Region']}),
        ('Change Details', {
            'fields': ['Summary', 'Description', 'Change_Details', 'Site_code', 'Configuration_Item']}),
        ('Implementation Details', {
            'fields': ['Plan_Owner', 'Plan_status', 'Change_Owner', 'Implementer', 'Validator']}),
        ('Implementation Status', {
            'fields': ['RFC_status', 'Change_status', 'CMC_Start_Notification', 'CMC_End_Notification',
                       'RFC_Task_closed', 'ROARS_IW_task_closed', 'RFC_Closed', 'Comments']}),

    ]

admin.site.register(Change, ChangeAdmin)

