"""Generated from Smithy shape ``com.amazonaws.invoicing#InvoiceCurrencyAmount``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.amount_breakdown
    import aws_sdk_invoicing.types.basic_string
    import aws_sdk_invoicing.types.currency_code
    import aws_sdk_invoicing.types.currency_exchange_details


class InvoiceCurrencyAmount(TypedDict):
    total_amount: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p> The invoice currency amount. </p>"""
    total_amount_before_tax: NotRequired[
        "aws_sdk_invoicing.types.basic_string.BasicString"
    ]
    """<p> Details about the invoice total amount before tax. </p>"""
    currency_code: NotRequired["aws_sdk_invoicing.types.currency_code.CurrencyCode"]
    """<p>The currency dominion of the invoice document.</p>"""
    amount_breakdown: NotRequired[
        "aws_sdk_invoicing.types.amount_breakdown.AmountBreakdown"
    ]
    """<p> Details about the invoice currency amount. </p>"""
    currency_exchange_details: NotRequired[
        "aws_sdk_invoicing.types.currency_exchange_details.CurrencyExchangeDetails"
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
        import aws_sdk_invoicing.types.amount_breakdown

        out["AmountBreakdown"] = (
            aws_sdk_invoicing.types.amount_breakdown.serialize_aws_json_1_0(
                value["amount_breakdown"]
            )
        )
    if "currency_exchange_details" in value:
        import aws_sdk_invoicing.types.currency_exchange_details

        out["CurrencyExchangeDetails"] = (
            aws_sdk_invoicing.types.currency_exchange_details.serialize_aws_json_1_0(
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
        import aws_sdk_invoicing.types.amount_breakdown

        out["amount_breakdown"] = (
            aws_sdk_invoicing.types.amount_breakdown.deserialize_aws_json_1_0(
                data["AmountBreakdown"]
            )
        )
    if "CurrencyExchangeDetails" in data:
        import aws_sdk_invoicing.types.currency_exchange_details

        out["currency_exchange_details"] = (
            aws_sdk_invoicing.types.currency_exchange_details.deserialize_aws_json_1_0(
                data["CurrencyExchangeDetails"]
            )
        )
    return out
