# -*- coding: utf-8 -*-
{
    'name': "Show Technical Name",

    'summary': """
        Show the technical name of each module in Apps 
        without the need to activate the debug mode.""",

    'description': """
        By installing this module, you will be able to see the technical name of each module in Apps without needing to activate debug mode.
    """,

    'author': "Faris Fathurrahman",
    'website': "https://frsfth25.wordpress.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        
        'views/ir_module_views.xml',

        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'auto_install': False,
}
