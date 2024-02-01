from odoo import models,fields,api
from datetime import date,datetime

class ToDoList(models.Model):
    _name="todo.task"
    _description="to do management"

    task_name = fields.Char(string="task name")
    assign_to_id = fields.Many2one(comodel_name="res.users", string="assign to")
    description = fields.Text(string="description")
    due_date = fields.Date(string="due date")
    status = fields.Selection([
        ('new','New'),
        ('inprogress','Inprogress'),
        ('completed','Completed'),
        ],string="status")
    estmated_time = fields.Datetime('estmated time')