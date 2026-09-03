#http://127.0.0.1:8000/api/method/guides_app.api.limited_greeting
import frappe
from frappe.rate_limiter import rate_limit


@frappe.whitelist(allow_guest=True)
@rate_limit(limit=5, seconds=60)
def limited_greeting():
    logger = frappe.logger()
    logger.info("Endpoint called.")

    frappe.response["message"] = "Hello, Rate Limited World!"


#only first 5 succeed.
# for i in {1..10}; do
#     echo "Request $i"
#     curl -s http://127.0.0.1:8000/api/method/guides_app.api.limited_greeting
#     echo
# done