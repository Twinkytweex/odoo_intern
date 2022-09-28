from odoo import models, api, fields
from . import workers


class Deprtment(models.Model):
    _name = 'department'
    _rec_name = 'compute_name'

    employe=fields.Char(string='იერარქია')
    parent_department = fields.Many2one('department', string='დეეპარტმანეტი')
    compute_name = fields.Char(string='სახელი', compute='_compute_name')

    @api.depends('employe', 'parent_department')
    def _compute_name(self):
        for rec in self:
            if rec.parent_department.employe:
                rec.compute_name = str(rec.parent_department.compute_name) + '/' + str(rec.employe)
            else:
                rec.compute_name = rec.employe
