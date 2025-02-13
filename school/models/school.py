from odoo import api, fields, models

class PracticeSchool(models.Model):
    _name = "school"
    _description = "School"

    name = fields.Char(string='School Name', required=True)
    students_ids = fields.One2many(comodel_name='school.students',inverse_name='school_id',string='Students')

