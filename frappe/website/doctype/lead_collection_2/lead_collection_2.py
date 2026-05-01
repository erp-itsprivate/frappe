# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class LeadCollection2(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		additional_info: DF.Text | None
		city: DF.Literal["", "\u062f\u0645\u0634\u0642", "\u0631\u064a\u0641 \u062f\u0645\u0634\u0642", "\u062d\u0644\u0628", "\u062d\u0645\u0635", "\u062d\u0645\u0627\u0647", "\u0627\u062f\u0644\u0628", "\u0637\u0631\u0637\u0648\u0633", "\u0627\u0644\u0644\u0627\u0630\u0642\u064a\u0629", "\u062f\u0631\u0639\u0627", "\u0627\u0644\u0633\u0648\u064a\u062f\u0627\u0621", "\u0627\u0644\u0642\u0646\u064a\u0637\u0631\u0629", "\u062f\u064a\u0631 \u0627\u0644\u0632\u0648\u0631", "\u0627\u0644\u062d\u0633\u0643\u0629", "\u0627\u0644\u0642\u0627\u0645\u0634\u0644\u064a"]
		custom_city_html: DF.Text | None
		custom_radio_html: DF.Text | None
		email_address: DF.Data | None
		first_name: DF.Data
		ip: DF.Data | None
		last_name: DF.Data
		model: DF.Literal["", "\u0633\u064a\u062f\u0627\u0646 Pegas", "\u0633\u064a\u062f\u0627\u0646 K3", "\u0633\u064a\u062f\u0627\u0646 K4", "SUV Sonet", "SUV Seltos", "SUV Sportage", "SUV Sorento", "MPV Carens", "MPV Carnival", "\u062a\u062c\u0627\u0631\u064a K2700", "\u062a\u062c\u0627\u0631\u064a K4000", "Other Other"]
		phone_number: DF.Data
	# end: auto-generated types
	pass
