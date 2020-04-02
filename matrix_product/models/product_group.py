# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class ProductGroup(models.Model):
    _name = "matrix_product.productgroup"
    _description = "Product Group"

    name = fields.Char(
        string='Product Group',
        required = True
    )
    code = fields.Char(
        string='Product Code',
        required = True,
        help='Two digit code'
    )