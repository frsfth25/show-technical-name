# -*- coding: utf-8 -*-
# from odoo import http


# class ShowTechnicalName(http.Controller):
#     @http.route('/show_technical_name/show_technical_name', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/show_technical_name/show_technical_name/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('show_technical_name.listing', {
#             'root': '/show_technical_name/show_technical_name',
#             'objects': http.request.env['show_technical_name.show_technical_name'].search([]),
#         })

#     @http.route('/show_technical_name/show_technical_name/objects/<model("show_technical_name.show_technical_name"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('show_technical_name.object', {
#             'object': obj
#         })
