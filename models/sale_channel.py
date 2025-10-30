from odoo import models, fields

class SaleChannel(models.Model):
    _name = 'sale.channel'
    _description = 'Canal de Venta'

    name = fields.Char(string='Nombre', required=True)
    code = fields.Char(string='Código', required=True)
    warehouse_id = fields.Many2one(
        'stock.warehouse',
        string='Depósito'
    )
    journal_id = fields.Many2one(
        'account.journal',
        string='Diario de Facturación'
    )

    _sql_constraints = [
        ('unique_code', 'unique(code)', 'El código del canal debe ser único.'),
    ]
