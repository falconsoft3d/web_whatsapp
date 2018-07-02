# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class company_zopim(models.Model):

    _description = "Company Zopim"
    _inherit = 'res.company'

    zopim = fields.Text('Zopim ID')
    num_what = fields.Integer(string='Number Whatsapp')
