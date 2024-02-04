# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class show_technical_name(models.Model):
#     _name = 'show_technical_name.show_technical_name'
#     _description = 'show_technical_name.show_technical_name'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
