from __future__ import unicode_literals
import frappe
from frappe.utils import cint, get_gravatar,flt,format_datetime, now_datetime,add_days,today,formatdate,date_diff,getdate,get_last_day
from frappe import throw, msgprint, _
from frappe.utils.password import update_password as _update_password
from frappe.desk.notifications import clear_notifications
from frappe.utils.user import get_system_managers
from erpnext.accounts.doctype.sales_invoice.sales_invoice import make_delivery_note
import frappe.permissions
import frappe.share
import re
import string
import random
import json
import time
from datetime import datetime
from datetime import date
from datetime import timedelta
import collections
import math
import logging
from operator import itemgetter 


@frappe.whitelist()
def checkAvailability(self,method):
	#frappe.msgprint("In Call")
	#self=frappe.get_doc("Patient Appointment",name)
	checkAppointment=frappe.get_all("Patient Appointment",filters={'appointment_date':self.appointment_date,'physician':self.physician,'appointment_time':self.appointment_time,'status':'Scheduled'},fields=["name"])
	if len(checkAppointment)>1:
		frappe.msgprint("Old")
		frappe.db.set_value("Patient Appointment", self.name, "status", "Waiting")
		return self.name
	else:
		frappe.msgprint("New")
		frappe.db.set_value("Patient Appointment", self.name, "status", "Scheduled")
		return self.name
	
