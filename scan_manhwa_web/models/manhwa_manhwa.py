"""Import"""
from odoo import fields, models

class Manhwa(models.Model):
    """Manhwa"""
    _name = "manhwa.manhwa"

    name = fields.Char()
    last_site = fields.Char()
    last_date = fields.Datetime()
    before_last_site = fields.Char()
    last_chapter = fields.FLoat()
    is_favorite = fields.Boolean()
    type = fields.Char()
    to_read = fields.Boolean()
    state = fields.Selection([('to_read', 'To read'), ('reading', 'Reading'), ('finished', 'Finished')])
    image = fields.Image()