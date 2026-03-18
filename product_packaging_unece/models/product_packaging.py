# Copyright 2026 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductPackaging(models.Model):

    _inherit = "product.packaging"

    unece_code = fields.Char(
        string="UNECE Code",
        help="Standard nomenclature of the United Nations Economic "
        "Commission for Europe (UNECE).",
        compute="_compute_unece_code",
        store=True,
        readonly=False,
    )

    @api.depends("packaging_level_id")
    def _compute_unece_code(self):
        for rec in self:
            if rec.packaging_level_id and rec.packaging_level_id.unece_code:
                rec.unece_code = rec.packaging_level_id.unece_code
