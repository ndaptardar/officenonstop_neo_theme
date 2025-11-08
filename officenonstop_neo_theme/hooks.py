app_name = "officenonstop_neo_theme"
app_title = "Officenonstop Neo Theme"
app_publisher = "You"
app_description = "Next-generation ERPNext v15 theme with light and dark color schemes, inspired by modern SaaS dashboards."
app_icon = "octicon octicon-color-mode"
app_color = "blue"
app_email = "you@example.com"
app_license = "MIT"

app_include_css = "/assets/officenonstop_neo_theme/css/theme.css"
app_include_js = "/assets/officenonstop_neo_theme/js/theme-switcher.js"

boot_session = "officenonstop_neo_theme.api.inject_theme_scheme"
after_install = "officenonstop_neo_theme.install.after_install"
