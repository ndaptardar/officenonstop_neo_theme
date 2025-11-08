import frappe

def after_install():
    """Ensure the User table has the theme column on installation."""
    if not frappe.db.has_column("User", "officenonstop_neo_theme_scheme"):
        frappe.db.sql("ALTER TABLE `tabUser` ADD COLUMN `officenonstop_neo_theme_scheme` VARCHAR(140)")
        frappe.db.commit()
