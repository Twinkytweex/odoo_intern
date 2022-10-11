from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
from datetime import date
from . import departament , personality

def _get_default_color(self):
    return randint(1,11)

class Information(models.Model):
    _name = 'workers'
    _inherit = ['hr.employee','mail.thread']
    #personal info
    depatments = fields.Many2one('department', 'დეპარტამენტი', required=True, )
    personality = fields.Many2many('persnality', string='პიროვნული თვისებები', required=True)
