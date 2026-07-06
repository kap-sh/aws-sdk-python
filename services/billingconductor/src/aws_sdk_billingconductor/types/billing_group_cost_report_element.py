"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupCostReportElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.aws_cost
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.currency
    import aws_sdk_billingconductor.types.margin
    import aws_sdk_billingconductor.types.margin_percentage
    import aws_sdk_billingconductor.types.proforma_cost


class BillingGroupCostReportElement(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"]
    """<p>The Amazon Resource Name (ARN) of a billing group.</p>"""
    aws_cost: NotRequired["aws_sdk_billingconductor.types.aws_cost.AWSCost"]
    """<p>The actual Amazon Web Services charges for the billing group.</p>"""
    proforma_cost: NotRequired[
        "aws_sdk_billingconductor.types.proforma_cost.ProformaCost"
    ]
    """<p>The hypothetical Amazon Web Services charges based on the associated pricing plan of a billing group.</p>"""
    margin: NotRequired["aws_sdk_billingconductor.types.margin.Margin"]
    """<p>The billing group margin.</p>"""
    margin_percentage: NotRequired[
        "aws_sdk_billingconductor.types.margin_percentage.MarginPercentage"
    ]
    """<p>The percentage of billing group margin.</p>"""
    currency: NotRequired["aws_sdk_billingconductor.types.currency.Currency"]
    """<p>The displayed currency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupCostReportElement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "aws_cost" in value:
        out["AWSCost"] = value["aws_cost"]
    if "proforma_cost" in value:
        out["ProformaCost"] = value["proforma_cost"]
    if "margin" in value:
        out["Margin"] = value["margin"]
    if "margin_percentage" in value:
        out["MarginPercentage"] = value["margin_percentage"]
    if "currency" in value:
        out["Currency"] = value["currency"]
    return out


def deserialize_json(data: dict) -> BillingGroupCostReportElement:
    out: BillingGroupCostReportElement = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "AWSCost" in data:
        out["aws_cost"] = data["AWSCost"]
    if "ProformaCost" in data:
        out["proforma_cost"] = data["ProformaCost"]
    if "Margin" in data:
        out["margin"] = data["Margin"]
    if "MarginPercentage" in data:
        out["margin_percentage"] = data["MarginPercentage"]
    if "Currency" in data:
        out["currency"] = data["Currency"]
    return out
