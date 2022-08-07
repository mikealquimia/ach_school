# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CategoryGrade(models.Model):
    _name = "category.grade"
    _description = "Grade for Students"

    name = fields.Char(string='Grade', required=True)
    course_ids = fields.Many2many('grade.course', string='Courses')
    teacher_in_charge_id = fields.Many2one('school.teacher', string='Teacher in Charge', domain=[('teacher_in_charge_id','=',True)])
    teacher_ids = fields.Many2many('school.teacher', string='Teachers')
    category_id = fields.Many2one('school.category', string='Category', required=True, domain="[('school_id','=',school_id)]")
    student_ids = fields.Many2many('grade.student', string='Student')
    school_id = fields.Many2one('school.school', string='School', required=True)