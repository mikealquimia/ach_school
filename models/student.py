# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SchoolStudent(models.Model):
    _name = "grade.student"

    name = fields.Char(string='Student')
    age = fields.Integer(string='Age')
    teacher_in_charge_id = fields.Many2one('school.teacher', string='Teacher in Charge', related="grade_id.teacher_in_charge_id")
    teacher_ids = fields.Many2many('school.teacher', string='Teachers')
    course_ids = fields.Many2many('grade.course', string='Courses')
    grade_id = fields.Many2one('category.grade', string='Grade', domain="[('school_id','=',school_id)]")
    category_id = fields.Many2one('school.category', string='Category', related="grade_id.category_id")
    school_id = fields.Many2one('school.school', string='School', required=True)
    
    parent_id = fields.Manyone('res.partner', string='Parent')
    