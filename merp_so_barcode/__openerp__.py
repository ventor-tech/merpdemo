# -*- coding: utf-8 -*-
{
    'name': 'Barcode on SO Printed Form',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        The current module is adding barcode to Printed Form of SO
        It is used just for demo purposes
        
    """,
    'author': 'Xpansa Group',
    'website': 'www.xpansa.com',
    'depends': ["base",'stock'],
    'init_xml': [],
    'data': [
        "views/report_salesorder.xml",
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
