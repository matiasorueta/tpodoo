{
    'name': 'Sale Channel Extension',
    'version': '1.0',
    'depends': ['sale_management', 'stock', 'account'],
    'data': [
        'views/sale_order_views.xml',
        'views/sale_channel_views.xml',
        
    ],
    'installable': True,
    'application': False,
}
