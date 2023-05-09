from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    # create a delivery order
    # ield (Dimension:) in stock move that read from sale order line also make this field editable (user can edit this field and this will NOT reflect the sale order line)
    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            for line in order.order_line:
                line.move_ids.write({'dimension': line.dimension})
        return res






