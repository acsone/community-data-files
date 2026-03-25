# Copyright 2026 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models
from odoo.tools import ormcache


class ProductPackagingLevel(models.Model):

    _inherit = "product.packaging.level"

    unece_type_ids = fields.Many2many(
        comodel_name="unece.code.list",
        string="UNECE Packaging Types",
        domain=[("type", "=", "packaging_type")],
        help="Select the Packaging Type Codes of the official "
        "nomenclature of the United Nations Economic "
        "Commission for Europe (UNECE), DataElement Rec 21)",
    )

    @api.model
    @ormcache("unece_code")
    def _get_packaging_level_ids_by_unece_code(self, unece_code):
        if not unece_code or not isinstance(unece_code, str):
            return []
        return self.search([("unece_type_ids.code", "=", unece_code)]).ids

    @api.model_create_multi
    def create(self, vals_list):
        records = super().create(vals_list)
        self._get_packaging_level_ids_by_unece_code.clear_cache(self)
        return records

    def write(self, vals):
        res = super().write(vals)
        self._get_packaging_level_ids_by_unece_code.clear_cache(self)
        return res

    def unlink(self):
        res = super().unlink()
        self._get_packaging_level_ids_by_unece_code.clear_cache(self)
        return res
