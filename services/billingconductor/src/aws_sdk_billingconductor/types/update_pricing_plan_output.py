"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdatePricingPlanOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.instant
    import aws_sdk_billingconductor.types.number_of_associated_pricing_rules
    import aws_sdk_billingconductor.types.pricing_plan_arn
    import aws_sdk_billingconductor.types.pricing_plan_description
    import aws_sdk_billingconductor.types.pricing_plan_name


class UpdatePricingPlanOutput(TypedDict):
    arn: NotRequired["aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"]
    """<p>The Amazon Resource Name (ARN) of the updated pricing plan. </p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_name.PricingPlanName"
    ]
    """<p> The name of the pricing plan. The name must be unique to each pricing plan. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_description.PricingPlanDescription"
    ]
    """<p> The new description for the pricing rule. </p>"""
    size: "aws_sdk_billingconductor.types.number_of_associated_pricing_rules.NumberOfAssociatedPricingRules"
    """<p> The pricing rules count that's currently associated with this pricing plan list. </p>"""
    last_modified_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p> The most recent time when the pricing plan was modified. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingPlanOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Size"] = value.get("size", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    return out


def deserialize_json(data: dict) -> UpdatePricingPlanOutput:
    out: UpdatePricingPlanOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if "LastModifiedTime" in data:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    return out
