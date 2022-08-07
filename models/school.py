# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolSchool(models.Model):
    _name = "school.school"

    name = fields.Char(string='School')
    company_id = fields.Many2one('res.compamy', string='Company', required=True)
    location_id = fields.Many2one('stock.warehouse', string='Warehouse', required=True)
    partner_id = fields.Many2one('res.partner', string='Street', required=True)