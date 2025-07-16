# proposal_generator/hooks.py

app_name = "erpnext_proposal_generator"
app_title = "Proposal Generator"
app_publisher = "Mangotek"
app_description = "Custom Proposal Management System for ERPNext"
app_icon = "octicon octicon-file-directory-fill"
app_color = "blue"
app_email = "admin@mangotek.com.au"
app_license = "MIT"

doc_events = {
    "Proposal": {
        "on_submit": "proposal_generator.utils.proposal.convert_to_contract"
    }
}

after_install = "proposal_generator.utils.install.after_install"
