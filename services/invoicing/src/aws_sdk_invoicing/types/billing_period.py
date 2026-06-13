"""Generated from Smithy shape ``com.amazonaws.invoicing#BillingPeriod``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.month
    import aws_sdk_invoicing.types.year


class BillingPeriod(TypedDict):
    month: "aws_sdk_invoicing.types.month.Month"
    """<p> The billing period month. </p>"""
    year: "aws_sdk_invoicing.types.year.Year"
    """<p> The billing period year. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingPeriod) -> dict:
    out: dict = {}
    out["Month"] = value["month"]
    out["Year"] = value["year"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BillingPeriod:
    out: BillingPeriod = {}  # type: ignore[typeddict-item]
    if "Month" in data:
        out["month"] = data["Month"]
    else:
        raise DeserializationError("BillingPeriod.month required")
    if "Year" in data:
        out["year"] = data["Year"]
    else:
        raise DeserializationError("BillingPeriod.year required")
    return out
