# proposal_generator/utils/crm_integration.py

import frappe

def get_details(ref):
    if not ref:
        return {}
    doctype = frappe.db.get_value("DocType", {"name": ref}, "doctype")
    if doctype == "Lead":
        lead = frappe.get_doc("Lead", ref)
        return {
            "customer": None,
            "contact": lead.email_id
        }
    elif doctype == "Opportunity":
        opp = frappe.get_doc("Opportunity", ref)
        return {
            "customer": opp.party_name,
            "contact": opp.contact_email
        }
    return {}
