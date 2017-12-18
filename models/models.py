# -*- coding: utf-8 -*-
from . import Tasca
from odoo import models, fields, api

# class llista_tasques(models.Model):
#     _name = 'llista_tasques.llista_tasques'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100