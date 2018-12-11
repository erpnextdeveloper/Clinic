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
import traceback


#custom:This function use to decide what is appointment status

@frappe.whitelist()
def app_error_log(title,error):
	d = frappe.get_doc({
			"doctype": "Custom Error Log",
			"title":str("User:")+str(title+" "+"App Name:Clinic"),
			"error":traceback.format_exc()
		})
	d = d.insert(ignore_permissions=True)
	return d


@frappe.whitelist()
def checkAvailability(self,method):
	try:
		checkAppointment=frappe.get_all("Patient Appointment",filters={'appointment_date':self.appointment_date,'physician':self.physician,'appointment_time':self.appointment_time,'status':'Scheduled'},fields=["name"])
		if len(checkAppointment)>1:
			frappe.msgprint("Old")
			frappe.db.set_value("Patient Appointment", self.name, "status", "Waiting")
			return self.name
		else:
			frappe.msgprint("New")
			frappe.db.set_value("Patient Appointment", self.name, "status", "Scheduled")
			return self.name

	except Exception as e:
		return generateResponse("F",error=e)




		
	
