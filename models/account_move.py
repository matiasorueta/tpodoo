from odoo import models, fields

class AccountMove(models.Model):
    _inherit = 'account.move'

    canal_venta_id = fields.Many2one('sale.channel', string='Canal de Venta')
