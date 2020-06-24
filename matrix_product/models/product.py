# -*- coding: utf-8 -*-

from odoo import api, models, fields, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    show_portal = fields.Boolean(string="Don't Show on Portal")
    product_group = fields.Many2one('matrix_product.productgroup',
        string='Product Group', required=True)

    seq = fields.Integer(
        string='Sequence',
        default=0,
        compute='_compute_sequence'
         )
        
    @api.depends('barcode')
    def _compute_sequence(self):
        for rec in self:
            if rec.barcode == False:
                code = self.env.ref('matrix_product.product_sequence_matrix').code
                rec.seq = self.env['ir.sequence'].next_by_code(code)


    @api.onchange('product_group')
    def onchange_group(self):
        for rec in self:
            if rec.product_group:
                if rec.barcode:
                    seq = rec.barcode.split('.')[1] 
                else:
                    seq = str(rec.seq)
                barcode = rec.product_group.code + '.' + seq
                rec.barcode = barcode

class Product(models.Model):
    _inherit = 'product.product'

    seq = fields.Integer(
        string='Sequence',
        default=0,
        stored=True,
        compute='_compute_sequence'
         )
        
    
    @api.depends('barcode')
    def _compute_sequence(self):
        for rec in self:
            if rec.barcode == False:
                code = self.env.ref('matrix_product.product_sequence_matrix').code
                rec.seq = self.env['ir.sequence'].next_by_code(code)

    @api.onchange('product_group')
    def onchange_group(self):
        for rec in self:
            if rec.product_group:
                if rec.barcode:
                    seq = rec.barcode.split('.')[1] 
                else:
                    seq = str(rec.seq)
                barcode = rec.product_group.code + '.' + seq
                rec.barcode = barcode