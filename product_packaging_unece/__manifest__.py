# Copyright 2026 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Product Packaging UNECE",
    "summary": """UNECE nomenclature for product packaging""",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/community-data-files",
    "depends": ["product_packaging_level", "base_unece"],
    "data": [
        "data/unece_tax_type.xml",
        "views/unece_code_list.xml",
        "views/product_packaging_level.xml",
    ],
}
