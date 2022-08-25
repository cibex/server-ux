from odoo import fields, models


class TestDateRangeSearchMixin(models.Model):
    _name = "test.date.range.search.mixin"
    _inherit = ["date.range.search.mixin"]
    _description = "Test Mixin class to add a Many2one style period search field"
    _date_range_search_field = "test_date"

    name = fields.Char()
    test_date = fields.Date()
