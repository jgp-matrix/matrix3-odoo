# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_group = fields.Many2one('matrix_product.productgroup',
        string='Product Group', required=True)

    
    @api.onchange('product_group', 'barcode')
    def onchange_group(self):
        for rec in self:
            if rec.product_group and rec.barcode:
                barcode_num = rec.barcode.split('.')[1] if '.' in rec.barcode else rec.barcode
                barcode = rec.product_group.code + '.' + barcode_num
                rec.barcode = barcode

class Product(models.Model):
    _inherit = 'product.product'

    @api.onchange('product_group', 'barcode')
    def onchange_group(self):
        for rec in self:
            if rec.product_group and rec.barcode:
                barcode_num = rec.barcode.split('.')[1] if '.' in rec.barcode else rec.barcode
                barcode = rec.product_group.code + '.' + barcode_num
                rec.barcode = barcode