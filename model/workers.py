from odoo import models, api, fields, _
from odoo.exceptions import ValidationError
from datetime import date
from . import departament


class Information(models.Model):
    _name = 'workers'
    _rec_name = 'first_name'
    #personal info
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

    depatments=fields.Many2one('department','დეპარტამენტი',required=True,)

    #department adding

    #constrains

    @api.constrains('id_numb')
    def _check_value(self):
        if len(self.id_numb) != 11:
            raise ValidationError(_('Enter Value 11'))

    # @api.constrains('expiration_date','birth_date')
    # def _check_expiration_date(self):
    #     birthday= birth_date
    #     for rec in self:
    #         if birthday <= rec.expiration_date:
    #             raise ValidationError(_("ვადის გასვლის თარიღი არასწორია !"))

    @api.constrains('birth_date')
    def _check_birth_date(self):
        for rec in self:
            if rec.birth_date > fields.Date.today():
                raise ValidationError(_("დაბადების თარიღი აღემატება მომავალში ვერ დაიბადები!"))