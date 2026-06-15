"""Generated from Smithy shape ``com.amazonaws.billingconductor#BillingGroupCostReportResultElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.attributes_list
    import aws_sdk_billingconductor.types.aws_cost
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.currency
    import aws_sdk_billingconductor.types.margin
    import aws_sdk_billingconductor.types.margin_percentage
    import aws_sdk_billingconductor.types.proforma_cost


class BillingGroupCostReportResultElement(TypedDict):
    arn: NotRequired["aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"]
    """<p>The Amazon Resource Number (ARN) that uniquely identifies the billing group.</p>"""
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
    """<p>The percentage of the billing group margin.</p>"""
    currency: NotRequired["aws_sdk_billingconductor.types.currency.Currency"]
    """<p>The displayed currency.</p>"""
    attributes: NotRequired[
        "aws_sdk_billingconductor.types.attributes_list.AttributesList"
    ]
    r"""<p>The list of key-value pairs that represent the attributes by which the <code>BillingGroupCostReportResults</code> are grouped. For example, if you want the Amazon S3 service-level breakdown of a billing group for November 2023, the attributes list will contain a key-value pair of <code>\"PRODUCT_NAME\"</code> and <code>\"S3\"</code> and a key-value pair of <code>\"BILLING_PERIOD\"</code> and <code>\"Nov 2023\"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillingGroupCostReportResultElement) -> dict:
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
    if "attributes" in value:
        import aws_sdk_billingconductor.types.attributes_list

        out["Attributes"] = (
            aws_sdk_billingconductor.types.attributes_list.serialize_json(
                value["attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> BillingGroupCostReportResultElement:
    out: BillingGroupCostReportResultElement = {}  # type: ignore[typeddict-item]
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
    if "Attributes" in data:
        import aws_sdk_billingconductor.types.attributes_list

        out["attributes"] = (
            aws_sdk_billingconductor.types.attributes_list.deserialize_json(
                data["Attributes"]
            )
        )
    return out
