# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolTeacherType(models.Model):
    _name = "school.teacher.type"
    _description = "Manager, teacher, substitute, director, etc."

    name = fields.Char(string='Teacher Type')
    school_id = fields.Many2one('school.school', string='School', required=True)
