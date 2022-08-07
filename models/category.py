# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolCategory(models.Model):
    _name = "school.category"
    _description = "Grouping of grades, kinder, primary, secondary, etc."

    name = fields.Char(string='Category', required=True)
    headmistress_id = fields.Many2one('school.teacher', string='Headmistress', domain=[('is_headmistress','=',True)])
    teacher_ids = fields.Many2many('school.teacher', string='Teachers')
    school_id = fields.Many2one('school.school', string='School', required=True)