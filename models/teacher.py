# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolTeacher(models.Model):
    _name = "school.teacher"

    name = fields.Char(string='Teacher')
    courses_ids = fields.One2many('grade.course', 'teacher_id', string='Courses')
    alternate_courses_ids = fields.One2many('category.course', 'alternate_teacher_id', string='Alternate Courses')
    category_ids = fields.Many2many('school.category', string='Category Grade')
    type = fields.Many2one('school.teacher.type', string='Type teacher', domain="[('school_id','=',school_id)]")
    school_id = fields.Many2one('school.school', string='School', required=True)
    is_teacher_in_charge = fields.Boolean(string="Is Teacher in Charge?")
    is_headmistress = fields.Boolean(string="Is Headmistress?")
    employe_id = fields.Many2one('hr.employee', string='Employee')
    