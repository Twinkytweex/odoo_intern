from odoo import http
from odoo.http import request, Response
import json

class Worker_control(http.Controller):
    @http.route(['/employee/workers'], type='http', auth='public',website=True, csrf=False,)
    def personal_employes(self):
        employs_rec = request.env['workers'].sudo().search([]).read([
            'first_name',
            'last_name',
            'city',
            'gender',
            'citizenship',
            'card_num',
        ])

        return Response(json.dumps(employs_rec,indent=4,sort_keys=False), content_type="application/json;charset=utf-8", status=200,)



