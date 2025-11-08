(function () {
  var storageKey = "officenonstop_neo_scheme";
  var schemes = ["light", "ocean", "sunset", "forest"];
  var classPrefix = "scheme-";

  function applyScheme(name) {
    var html = document.documentElement;
    schemes.forEach(s => html.classList.remove(classPrefix + s));
    if (schemes.includes(name)) html.classList.add(classPrefix + name);
  }

  function saveLocal(name) {
    try { localStorage.setItem(storageKey, name); } catch (e) {}
  }
  function loadLocal() {
    try { return localStorage.getItem(storageKey) || null; } catch (e) { return null; }
  }

  async function saveRemote(name) {
    if (window.frappe && frappe.call) {
      await frappe.call({
        method: "officenonstop_neo_theme.api.save_theme_scheme",
        args: { scheme: name },
        freeze: false
      });
    }
  }

  function createUI() {
    if (document.getElementById("theme-switcher-floating")) return;
    var wrap = document.createElement("div");
    wrap.id = "theme-switcher-floating";
    wrap.className = "theme-switcher-floating";
    schemes.forEach(s => {
      var btn = document.createElement("button");
      btn.className = "theme-switcher-btn";
      btn.dataset.scheme = s;
      btn.title = "Switch to " + s;
      btn.onclick = async () => {
        applyScheme(s);
        saveLocal(s);
        await saveRemote(s);
      };
      wrap.appendChild(btn);
    });
    document.body.appendChild(wrap);
  }

  function init() {
    var saved = (window.frappe && frappe.boot && frappe.boot.officenonstop_neo_theme_scheme) || loadLocal() || "light";
    applyScheme(saved);
    saveLocal(saved);
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", createUI);
    } else createUI();
  }

  init();
})();