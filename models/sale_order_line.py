from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    dimension = fields.Char(string="dimension")


    # create invoice
    #  field Dimension  in account invoice line that read from stock move dimension NOT the dimension of sale order line
    def _prepare_invoice_line(self, **optional_values):
        print("88888888888888 try invoice ")
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        res.update({
               'dimension': self.move_ids.dimension

            })

        return res





