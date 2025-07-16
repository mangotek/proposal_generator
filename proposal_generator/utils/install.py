# proposal_generator/utils/install.py

def after_install():
    from frappe import _
    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
    from frappe.custom.doctype.property_setter.property_setter import make_property_setter

    custom_fields = {
        "Proposal": [
            dict(
                fieldname="naming_series",
                label=_("Naming Series"),
                fieldtype="Data",
                options="PROJ-.YYYY.-",
                insert_after="title"
            ),
            dict(
                fieldname="lead_opportunity",
                label=_("Lead / Opportunity"),
                fieldtype="Dynamic Link",
                options="reference_doctype",
                insert_after="customer"
            )
        ]
    }

    create_custom_fields(custom_fields)

    # Make fields read-only for non-admin roles
    make_property_setter("Proposal", "profit_margin", "read_only", 1, "Check")
