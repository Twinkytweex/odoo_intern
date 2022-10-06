from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
from datetime import date
from . import departament , personality

def _get_default_color(self):
    return randint(1,11)

class Information(models.Model):
    _name = 'workers'
    _rec_name = 'position'
    _inherit = ['mail.thread']
    #personal info
    picture = fields.Binary(
        comodel_name='ir.attachment',
        attachment=True,
        string="სურათი",
        store=True,
    )
    position = fields.Char(
        string= "პოზიცია",
        required=True,
        size=20,
    )
    first_name = fields.Char(
        string="სახელი",
        required=True,
        size=20,
    )
    last_name= fields.Char(
        string="გვარი",
        required=True,
        size=20
    )
    city= fields.Selection([
        ("Tbilisi", "თბილისი"),
        ("Batumi", "ბათუმი"),
        ("Kutaisi", "ქუთაისი"),
        ("Zestafoni", "ზესტაფონი"),
    ],
        required=True,
        string='ქალაქი')
    gender=fields.Selection([
        ("Men", "კაცი"),
        ("Women", "ქალი"),
    ],
        required=True,
        string='სქესი')
    citizenship=fields.Selection([
        ("Georgia", "საქართველო"),
        ("Foreign country", "უცხო ქვეყნის მოქალაქე"),
    ],
        required=True,
        string='მოქალაქეობა')
    card_num=fields.Char(
        size=11,
        string='ბარათის ნომერი',
        required=True
    )
    id_numb=fields.Char(
        string='პირადი ნომერი',
        size=11,
        required=True,
    )
    birth_date=fields.Date(
        string='დაბადების თარიღი',
        required=True
    )
    expiration_date=fields.Date(
        string='გაუქმების თარიღი',
        required=True
    )
    color_choice = fields.Integer(
        string='ფერი_ციფრებისთვის'
    )
    comment_section = fields.Text(
        string="კომენტარები",
        size=250,
    )
    mobile_phone = fields.Char(
        string="ტელეფონის ნომერი",
        required=True,
        size=9,
    )
    em_ail = fields.Char(
        string="შეიყვანეთ თქვენი ფოსტა",
        required=True,
    )

    depatments=fields.Many2one('department','დეპარტამენტი',required=True,)
    personality=fields.Many2many('persnality',string='პიროვნული თვისებები',required=True)

    #constrains

    @api.constrains('id_numb')
    def _check_value(self):
        if len(self.id_numb) != 11:
            raise ValidationError(_('Enter Value 11'))
        elif not self.id_numb.isdigit():
            raise ValidationError(_('enter only numbers'))

    @api.constrains('birth_date')
    def _check_birth_date(self):
        for rec in self:
            if rec.birth_date > fields.Date.today():
                raise ValidationError(_("დაბადების თარიღი აღემატება მომავალში ვერ დაიბადები!"))
