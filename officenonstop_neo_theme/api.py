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
    """Inject user theme scheme into frappe bootinfo with column safety."""
    user = frappe.session.user

    # Safety check: create column if missing
    if not frappe.db.has_column("User", "officenonstop_neo_theme_scheme"):
        frappe.db.add_column("User", "officenonstop_neo_theme_scheme", "Data")
        frappe.db.commit()

    # Get scheme or fallback
    scheme = frappe.db.get_value("User", user, "officenonstop_neo_theme_scheme") or "light"
    bootinfo.officenonstop_neo_theme_scheme = scheme
