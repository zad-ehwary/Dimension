from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = "stock.move"

    dimension = fields.Char(string="Dimension", store=True, )


