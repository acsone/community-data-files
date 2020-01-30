# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class UneceCodeList(models.Model):
    _inherit = "unece.code.list"

    type = fields.Selection(
        selection_add=[
            ("meat_species", "Species"),
            ("meat_product_cut", "Product/cut"),
            ("meat_refrigeration", "Refrigeration"),
            ("meat_bovine_category", "Bovine category"),
            ("meat_production_system", "Production system"),
            ("meat_feeding_system", "Feeding system"),
            ("meat_slaughter_system", "Slaughter system"),
            ("meat_post_slaughter_system", "Post-slaughter system"),
            ("meat_fat_thickness", "Fat thickness"),
            ("meat_bovine_quality_system", "Bovine quality system"),
            ("meat_weight_range", "Weight range"),
            ("meat_packing", "Packing"),
            ("meat_conformity_assessment", "Conformity assessment"),
        ]
    )
