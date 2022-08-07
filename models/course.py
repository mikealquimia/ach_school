# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GradeCourse(models.Model):
    _name = "grade.course"
    _description = "Courses for students"

    name = fields.Char(string='Course', required=True)
    grade_id = fields.Many2one('category.grade', string='Grade', domain="[('school_id','=',school_id)]", required=True)
    teacher_id = fields.Many2one('school.teacher', string='Teacher', domain="[('school_id','=',school_id)]", required=True)
    alternate_teacher_id = fields.Manyone('school.teacher', string='Alternate Teacher', domain="[('school_id','=',school_id)]")
    category_id = fields.Many2one('school.category', string='Category', related="grade_id.category_id")
    student_ids = fields.Many2many('grade.student', string='Students')
    school_id = fields.Many2one('school.school', string='School')