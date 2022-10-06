from odoo import models, api, fields
from . import workers

class Personality(models.Model):
    _name='persnality'
    _rec_name = 'personality_of_employ'

    personality_of_employ= fields.Char(string='დახასიათება',)
    color = fields.Integer(string="color")
