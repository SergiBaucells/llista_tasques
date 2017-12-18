# -*- coding: utf-8 -*-
from odoo import http

# class LlistaTasques(http.Controller):
#     @http.route('/llista_tasques/llista_tasques/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/llista_tasques/llista_tasques/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('llista_tasques.listing', {
#             'root': '/llista_tasques/llista_tasques',
#             'objects': http.request.env['llista_tasques.llista_tasques'].search([]),
#         })

#     @http.route('/llista_tasques/llista_tasques/objects/<model("llista_tasques.llista_tasques"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('llista_tasques.object', {
#             'object': obj
#         })