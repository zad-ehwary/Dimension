# -*- coding: utf-8 -*-
# from odoo import http


# class MysaleOrder(http.Controller):
#     @http.route('/mysale_order/mysale_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mysale_order/mysale_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('mysale_order.listing', {
#             'root': '/mysale_order/mysale_order',
#             'objects': http.request.env['mysale_order.mysale_order'].search([]),
#         })

#     @http.route('/mysale_order/mysale_order/objects/<model("mysale_order.mysale_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mysale_order.object', {
#             'object': obj
#         })
