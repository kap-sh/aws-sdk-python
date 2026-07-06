"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#InvoiceBillingPeriod``."""

from typing_extensions import TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError


class InvoiceBillingPeriod(TypedDict, closed=True):
    month: "int"
    """<p>The billing period month. Valid range: 1-12.</p>"""
    year: "int"
    """<p>The billing period year.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvoiceBillingPeriod) -> dict:
    out: dict = {}
    out["month"] = value["month"]
    out["year"] = value["year"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvoiceBillingPeriod:
    out: InvoiceBillingPeriod = {}  # type: ignore[typeddict-item]
    if "month" in data:
        out["month"] = data["month"]
    else:
        raise DeserializationError("InvoiceBillingPeriod.month required")
    if "year" in data:
        out["year"] = data["year"]
    else:
        raise DeserializationError("InvoiceBillingPeriod.year required")
    return out
