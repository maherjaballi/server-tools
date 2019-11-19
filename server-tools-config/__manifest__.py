# © 2019  Vauxoo (<http://www.vauxoo.com/>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Server Tools Configuration',
    'version': '12.0.1.0.0',
    'author': 'TenovarLTD',
    'website': 'https://www.tenovar.com',
    'description' : """Server Tools Configuration""",
    'license': 'AGPL-3',
    'category': 'Tools',
    'depends': [
        'base_setup',
    ],
    'data': [        
        'views/res_config_settings_views.xml',       
    ],
    'installable': True,
    'auto_install': False,
    
}
