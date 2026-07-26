"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceCurrencyAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_invoicing.types.amount_breakdown
    import capo_invoicing.types.basic_string
    import capo_invoicing.types.currency_code
    import capo_invoicing.types.currency_exchange_details


class InvoiceCurrencyAmount(TypedDict, closed=True):
    total_amount: NotRequired["capo_invoicing.types.basic_string.BasicString"]
    """<p> The invoice currency amount. </p>"""
    total_amount_before_tax: NotRequired[
        "capo_invoicing.types.basic_string.BasicString"
    ]
    """<p> Details about the invoice total amount before tax. </p>"""
    currency_code: NotRequired["capo_invoicing.types.currency_code.CurrencyCode"]
    """<p>The currency dominion of the invoice document.</p>"""
    amount_breakdown: NotRequired[
        "capo_invoicing.types.amount_breakdown.AmountBreakdown"
    ]
    """<p> Details about the invoice currency amount. </p>"""
    currency_exchange_details: NotRequired[
        "capo_invoicing.types.currency_exchange_details.CurrencyExchangeDetails"
    ]
    """<p> The details of currency exchange. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceCurrencyAmount) -> dict:
    out: dict = {}
    if "total_amount" in value:
        out["TotalAmount"] = value["total_amount"]
    if "total_amount_before_tax" in value:
        out["TotalAmountBeforeTax"] = value["total_amount_before_tax"]
    if "currency_code" in value:
        out["CurrencyCode"] = value["currency_code"]
    if "amount_breakdown" in value:
        import capo_invoicing.types.amount_breakdown

        out["AmountBreakdown"] = (
            capo_invoicing.types.amount_breakdown.serialize_aws_json_1_0(
                value["amount_breakdown"]
            )
        )
    if "currency_exchange_details" in value:
        import capo_invoicing.types.currency_exchange_details

        out["CurrencyExchangeDetails"] = (
            capo_invoicing.types.currency_exchange_details.serialize_aws_json_1_0(
                value["currency_exchange_details"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceCurrencyAmount:
    out: InvoiceCurrencyAmount = {}  # type: ignore[typeddict-item]
    if "TotalAmount" in data:
        out["total_amount"] = data["TotalAmount"]
    if "TotalAmountBeforeTax" in data:
        out["total_amount_before_tax"] = data["TotalAmountBeforeTax"]
    if "CurrencyCode" in data:
        out["currency_code"] = data["CurrencyCode"]
    if "AmountBreakdown" in data:
        import capo_invoicing.types.amount_breakdown

        out["amount_breakdown"] = (
            capo_invoicing.types.amount_breakdown.deserialize_aws_json_1_0(
                data["AmountBreakdown"]
            )
        )
    if "CurrencyExchangeDetails" in data:
        import capo_invoicing.types.currency_exchange_details

        out["currency_exchange_details"] = (
            capo_invoicing.types.currency_exchange_details.deserialize_aws_json_1_0(
                data["CurrencyExchangeDetails"]
            )
        )
    return out
