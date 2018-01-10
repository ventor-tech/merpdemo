# -*- coding: utf-8 -*-
{
    'name': 'Demo Barcode Scanner',
    'version': '1.0',
    'category': '',
    "sequence": 14,
    'complexity': "easy",
    'category': 'Hidden',
    'description': """
        The current module is adding digital signature demo
        Digital signature is added to customer invoices. 
        * Go to menu Accounting -> Customer invoices
        * Enter Edit Mode
        * Click Button "Customer Signature"
        * Submit Signature and save invoice
        * Now click context menu add top-right corner, click Print - Invoice
        
    """,
    'author': 'Xpansa Group',
    'website': 'www.xpansa.com',
    'depends': ["base",'account'],
    'init_xml': [],
    'data': [
        "views/account_view.xml",
        "reports/account_report.xml",
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
