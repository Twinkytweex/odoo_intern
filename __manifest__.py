
{
    'name': 'Workers.module',
    'version': '1.0',
    'description': """ 
    Hello this is the begginer test of 
    odoo. Thank you for patience.
    """,
    'category' : 'Test',
    'author': 'sandro khvedelidze',
    'website':'sandroxvedo.com',
    'depends': ['base'],
    'data': [
        'view/information.xml',
        'report/record.xml',
        'report/good_worker.xml',
    ],
    # 'demo': ['demo.xml'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
