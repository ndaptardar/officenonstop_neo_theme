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
    user = frappe.session.user
    scheme = frappe.db.get_value("User", user, "officenonstop_neo_theme_scheme") or "light"
    bootinfo.officenonstop_neo_theme_scheme = scheme
