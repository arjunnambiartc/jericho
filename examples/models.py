from django.db import models
from django.contrib.auth.models import User


class Change(models.Model):
    RFC = models.CharField(max_length=100)
    Ticket_Number = models.CharField(max_length=100,
                                     help_text='MAC / Istrat / ROARS / Incident / TechDirect / eConnect')
    Plan_Owner = models.ForeignKey(User, related_name='plan_owner', null=False)
    User_Requested_Time = models.DateTimeField(help_text='in EST')
    Change_Owner = models.ForeignKey(User, related_name='change_owner', null=False, verbose_name='Change Owner')
    Start_Time = models.DateTimeField(help_text='in EST')
    End_Time = models.DateTimeField(help_text='in EST')
    User_Email = models.EmailField()
    Line_of_Business = models.CharField(max_length=100)
    Conf_Call_Details = models.TextField(blank=True,
                                         verbose_name='Conference Call details',
                                         help_text='Try and enter few some more lines')
    Plan_status_choices = ((1, 'Good to go,Reconfirmed with the user'), (2, 'Pending Engineering Approvals'),
                           (3, 'Pending Information from User'), (4, 'Pending Plan from GNAM'),
                           (5, 'Plan Validation Pending'), (6, 'Pending Peer Review Approval'),
                           (7, 'Pending PAC File Editing'), (8, 'Pending Cert Order'))
    Plan_status = models.SmallIntegerField(choices=Plan_status_choices, default=4, max_length=50)
    Region_Choice = ((1, 'AMRS'), (2, 'EMEA'), (3, 'PACRIM'))
    Region = models.SmallIntegerField(choices=Region_Choice, default=1, max_length=6)
    Summary = models.TextField(blank=True, verbose_name='Summary',
                               help_text='Try and enter few some more lines')
    Description = models.TextField(blank=True, verbose_name='Description',
                                   help_text='Try and enter few some more lines')
    Plan = models.TextField(blank=True, verbose_name='Plan')
    Change_Details = models.CharField(max_length=300)
    Site_code = models.CharField(max_length=20)
    Configuration_Item = models.TextField(blank=True, verbose_name='Configuration Item',
                                          help_text='Try and enter few some more lines')
    Change_status_choice = ((1, 'Not Yet Started'), (2, 'In Progress'), (3, 'Partially Completed'),
                            (4, 'Completed'), (5, 'Rescheduled'), (6, 'Cancelled'), (7, 'Reverted'),
                            (8, 'Failed'), (9, 'Duplicate Entry'), (10, 'No change required'),
                            (11, 'Transferred to IPAM'))

    Change_status = models.SmallIntegerField(choices=Change_status_choice, default=1, max_length=50)
    Implementer = models.ForeignKey(User, related_name='implementer', null=False)
    Validator = models.ForeignKey(User, related_name='validator', null=False)
    RFC_status_choice = ((1, 'Initial'), (2, 'Pending Assessment'), (3, 'Pending Requester Group Approvals'),
                        (4, 'Pending Group Approvals'), (5, 'Pending Final Approvals'), (6, 'Pending Implementation'),
                        (7, 'Implemented'), (8, 'Cancelled'), (9, 'Rejected'), (10, 'On Hold'), (11, 'No RFC Required'),
                        (12, 'Awaiting RFC details from GNAM'))

    RFC_status = models.SmallIntegerField(choices=RFC_status_choice, default=1, max_length=50)
    Yes_no_choice = ((1, 'Yes'), (2, 'No'), (3, 'N/A'))
    CMC_Start_Notification = models.SmallIntegerField(choices=Yes_no_choice, default=2, max_length=5)
    CMC_End_Notification = models.SmallIntegerField(choices=Yes_no_choice, default=2, max_length=5)
    RFC_Task_closed = models.SmallIntegerField(choices=Yes_no_choice, default=2, max_length=5)
    ROARS_IW_task_closed = models.SmallIntegerField(choices=Yes_no_choice, default=2,
                                                    verbose_name='ROARS/IW task closed', max_length=5)
    RFC_Closed = models.SmallIntegerField(choices=Yes_no_choice, default=2, max_length=5)
    Comments = models.TextField(blank=True, verbose_name='Comments',
                                help_text='Try and enter few some more lines', )

    def __unicode__(self):
        return self.RFC

