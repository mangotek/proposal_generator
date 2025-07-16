# proposal_generator/utils/proposal.py

import frappe

def convert_to_contract(doc, method=None):
    if doc.status != "Accepted":
        frappe.throw(_("Only accepted proposals can be converted to contracts."))

    contract = frappe.new_doc("Contract")
    contract.party_name = doc.customer
    contract.start_date = doc.valid_from
    contract.end_date = doc.valid_to
    contract.contract_terms = doc.terms_and_conditions
    contract.save()
    doc.contract = contract.name
    doc.save()
    frappe.msgprint(_("Contract {0} created successfully.").format(contract.name))


def calculate_profit_margin(doc, method=None):
    total_amount = sum(item.amount for item in doc.proposal_items)
    total_cost = sum((item.cost or 0) * (item.qty or 0) for item in doc.proposal_items)

    if total_amount > 0:
        margin = ((total_amount - total_cost) / total_amount) * 100
        doc.profit_margin = round(margin, 2)
