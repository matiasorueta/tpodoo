from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    canal_venta_id = fields.Many2one(
        'sale.channel',
        string='Canal de Venta',
        required=True,
    )

    @api.onchange('canal_id')
    def _onchange_canal_id(self):
        if self.canal_id:
            # Cuando cambia el canal, se asigna el depósito del canal
            self.warehouse_id = self.canal_id.warehouse_id.id

    def _prepare_invoice(self):
        vals = super()._prepare_invoice()
        if self.canal_id:
            # Guardar el canal en la factura
            vals['canal_id'] = self.canal_id.id

            # Asignar el diario de facturación del canal
            if self.canal_id.journal_id:
                vals['journal_id'] = self.canal_id.journal_id.id
        return vals
    
    def _prepare_picking(self):
        res = super()._prepare_picking()
        if self.canal_id:
            res['canal_venta_id'] = self.canal_id.id
        return res