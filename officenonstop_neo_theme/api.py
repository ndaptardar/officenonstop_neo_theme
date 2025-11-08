import frappe

@frappe.whitelist()
def save_theme_scheme(scheme: str):
    if not scheme:
        return
    valid_schemes = ["ocean", "sunset", "forest", "light"]
    if scheme not in valid_schemes:
        frappe.throw("Invalid scheme")
    user = frappe.session.user
    frappe.db.set_value("User", user, "officenonstop_neo_theme_scheme", scheme)
    frappe.db.commit()
    return {"message": f"Theme '{scheme}' saved for {user}"}

@frappe.whitelist()
def get_theme_scheme():
    user = frappe.session.user
    return frappe.db.get_value("User", user, "officenonstop_neo_theme_scheme") or "light"

def inject_theme_scheme(bootinfo):
    """Inject user theme scheme into frappe bootinfo safely, creating column if missing."""
    user = frappe.session.user

    # Check if column exists
    if not frappe.db.has_column("User", "officenonstop_neo_theme_scheme"):
        # Add column manually via SQL (since frappe.db.add_column is deprecated)
        frappe.db.sql("ALTER TABLE `tabUser` ADD COLUMN `officenonstop_neo_theme_scheme` VARCHAR(140)")
        frappe.db.commit()

    # Get user's current scheme, or default to light
    scheme = frappe.db.get_value("User", user, "officenonstop_neo_theme_scheme") or "light"
    bootinfo.officenonstop_neo_theme_scheme = scheme
