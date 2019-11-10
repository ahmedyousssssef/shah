# -*- coding: utf-8 -*-

from openerp import api, fields, models


class WorkingTime(models.TransientModel):
    _name = 'working.time.wiz'

    calendar_id = fields.Many2one(comodel_name="resource.calendar", string="Working Time", required=True, )
    employee_ids = fields.Many2many(comodel_name="hr.employee", string="Employees", )

    @api.multi
    def assign_working_time_to_employees(self):
        for record in self:
            if record.employee_ids and record.calendar_id:
                record.employee_ids.write({'calendar_id': record.calendar_id.id})
