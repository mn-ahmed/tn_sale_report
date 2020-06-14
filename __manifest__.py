# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "TN sale Report",
    'summary': """Tunisia based sale report""",
    'description': """
        ...
    """,
    'license': 'AGPL-3',
    'author': "	AHMED MNASRI",
    'website': "",
    'category': 'Sale',
    'version': '12.0.0.1.0',
    'depends': ['sale', ],
    'data': [
            #'views/sale_view.xml',
            'report/reports.xml',
            'report/sale_report_template.xml',
             ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
