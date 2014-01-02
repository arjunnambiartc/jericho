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
from .models import Change
from suit.admin import SortableTabularInline, SortableModelAdmin
from suit.widgets import SuitDateWidget, SuitSplitDateTimeWidget, EnclosedInput, LinkedSelect, AutosizedTextarea
from django_select2 import AutoModelSelect2Field, AutoHeavySelect2Widget
from mptt.admin import MPTTModelAdmin
from guardian.admin import GuardedModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin


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
            'Plan': AutosizedTextarea(attrs={'class': 'span8'}),
        }


class ChangeAdmin(ModelAdmin):
    form = ChangeForm
    search_fields = ('RFC', 'Ticket_Number', 'User_Email', 'Change_Details')
    list_display = ('RFC', 'Ticket_Number', 'User_Email', 'User_Requested_Time', 'Start_Time', 'End_Time',
                    'User_Email', 'Change_Details', 'Plan_Owner', 'Plan_status',
                    'Change_Owner', 'Change_status', 'Implementer', 'Validator')
    list_select_related = True
    list_filter = ('Start_Time', 'End_Time')
    fieldsets = [
        ('Ticket Details', {
            'classes': 'suit-tab suit-tab-general',
            'fields': ['RFC', 'Ticket_Number']}),
        ('Timelines', {
            'classes': 'suit-tab suit-tab-general',
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
        ('Attach Plan', {
            'classes': 'suit-tab suit-tab-plan',
            'fields': ['Plan']})

    ]

    def suit_cell_attributes(self, obj, column):
        if column == 'Plan_status' or column == 'Change_status' or column == 'Change_Details':
            return {'class': 'nowrap'}

    def suit_row_attributes(self, obj):
        class_map = {
            1: 'warning',
        }

        css_class = class_map.get(obj.Region_Choice)
        if css_class:
            return {'class': css_class}


    suit_form_tabs = (('general', 'General'), ('plan', 'Plan'))

admin.site.register(Change, ChangeAdmin)


