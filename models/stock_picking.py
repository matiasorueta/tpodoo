from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    canal_venta_id = fields.Many2one('sale.canal.venta', string='Canal de Venta')
