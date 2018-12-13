/*
(c) ESS 2015-16
*/
frappe.listview_settings['Client Treatment'] = {
	filters: [["status", "=", "Draft"]],
	get_indicator: function(doc) {

		if(doc.status=="Draft"){
			return [__("Pending"), "darkgrey", "status,=,Pending"];
		}
		if(doc.status=="Submitted"){
			return [__("Completed"), "purple", "status,=,Completed"];
		}


	},
};
