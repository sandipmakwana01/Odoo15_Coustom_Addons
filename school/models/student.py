from odoo import api, fields, models

class PracticeStudents(models.Model):
    _name = "school.students"
    _description = "School Students"

    name = fields.Char(string='Student Name',required=True)
    school_id = fields.Many2one(comodel_name='school',string='School')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')])
    display_type = fields.Selection(
        selection=[
            ('line_section', 'Section'),
            ('line_note', 'Note')
        ], readonly=True
    )

    # @api.model
    # def _read_group_display_type(self, categories, domain, order):
    #     """ Ensure display_type is grouped properly in tree views """
    #     return categories
