# -*- coding: utf-8 -*-
{
    'name': "Matrix System: Sequential Number for Barcode",

    'summary': """
       Adding product group number to the barcode
    """,

    'description': """
        Task ID: 2228019 - AAL
        
The client would like to have a sequence number for barcodes on product.template 
(and product.product). He has a studio field on product.template called 
Product Group (x_studio_product_group, type selection), he would like the sequence 
of the bar code to be 'FirstTwoDigitsofProductGroup.sequece'. According to the review 
from the development team, we will create another field called Product Group that will 
work the same way as the studio field, since we do not use Studio field for developments.
    """,

    'author': "Odoo PS-US",
    'website': "http://www.odoo.com",
    'license': 'OEEL-1',

    'category': 'Custom Development',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product','stock','sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/product_sequence.xml',
        'views/product_views_inherits.xml',
        'views/product_group.xml',
        'views/product_group_list.xml',
        'views/sale_order_document_inherit.xml',
    ],
}
