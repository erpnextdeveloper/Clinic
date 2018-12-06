from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Document"),
			"items": [
				{
					"type": "doctype",
					"name": "Doctor",
					"description": _("Doctor")
				},
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Client")
				},
				{
					"type": "doctype",
					"name": "Patient Appointment",
					"description": _("Client Appointment")
				},
				{
					"type": "doctype",
					"name": "Consultation",
					"description": _("Consultation")
				}

			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Doctor Designation",
					"description": _("Doctor Designation")
				},
				{
					"type": "doctype",
					"name": "Healthcare Settings",
					"description": _("Healthcare Settings")
				},
				{
					"type": "doctype",
					"name": "Physician Schedule",
					"description": _("Physician Schedule")
				}
			]



		}
	]
