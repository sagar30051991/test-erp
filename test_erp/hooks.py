# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "test_erp"
app_title = "test_erp"
app_publisher = "Frappe"
app_description = "Mange All doctype,report"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "sagar.s@indictranstech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/test_erp/css/test_erp.css"
# app_include_js = "/assets/test_erp/js/test_erp.js"

# include js, css files in header of web template
# web_include_css = "/assets/test_erp/css/test_erp.css"
# web_include_js = "/assets/test_erp/js/test_erp.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "test_erp.install.before_install"
# after_install = "test_erp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "test_erp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"test_erp.tasks.all"
# 	],
# 	"daily": [
# 		"test_erp.tasks.daily"
# 	],
# 	"hourly": [
# 		"test_erp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"test_erp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"test_erp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "test_erp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "test_erp.event.get_events"
# }

