import frappe

def after_install():
    """Automatically add missing column to User for theme persistence."""
    if not frappe.db.has_column("User", "officenonstop_neo_theme_scheme"):
        frappe.db.add_column("User", "officenonstop_neo_theme_scheme", "Data")
        frappe.db.commit()
