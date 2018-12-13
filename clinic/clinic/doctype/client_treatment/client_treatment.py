# -*- coding: utf-8 -*-
# Copyright (c) 2018, GreyCube Technologies and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class ClientTreatment(Document):
	def after_insert(self):
		frappe.db.set_value("Client Treatment",self.name,"status","Pending")

	def on_submit(self):
		frappe.db.set_value("Client Treatment",self.name,"status","Completed")
