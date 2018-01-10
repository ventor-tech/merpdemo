# -*- coding: utf-8 -*-
{
    'name': 'Demo Barcode Scanner',
    "version": "8.0.1.0.0",
    'author': 'Ventor, Xpansa Group',
    'website': 'https://ventor.tech/',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        The current module is adding ability to select product with barcode scanner
        Barcode scanner is using built-in mobile phone camera and supports most of standard codes
        Scanner is added to product field in menu Warehouse -> Tracebility -> Stock Moves
        
    """,
    'depends': ["base",'stock'],
    'init_xml': [],
    'data': [
        "views/stock_view.xml",
    ],
    'demo_xml': [],
    'test': [
    ],
    'qweb' : [
    ],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
