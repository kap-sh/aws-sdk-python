"""Generated from Smithy shape ``com.amazonaws.billingconductor#PricingPlanListElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.instant
    import aws_sdk_billingconductor.types.number_of_associated_pricing_rules
    import aws_sdk_billingconductor.types.pricing_plan_arn
    import aws_sdk_billingconductor.types.pricing_plan_description
    import aws_sdk_billingconductor.types.pricing_plan_name


class PricingPlanListElement(TypedDict):
    name: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_name.PricingPlanName"
    ]
    """<p>The name of a pricing plan.</p>"""
    arn: NotRequired["aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"]
    """<p>The pricing plan Amazon Resource Names (ARN). This can be used to uniquely identify a pricing plan.</p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_description.PricingPlanDescription"
    ]
    """<p>The pricing plan description.</p>"""
    size: "aws_sdk_billingconductor.types.number_of_associated_pricing_rules.NumberOfAssociatedPricingRules"
    """<p>The pricing rules count that's currently associated with this pricing plan list element.</p>"""
    creation_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p>The time when the pricing plan was created.</p>"""
    last_modified_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p>The most recent time when the pricing plan was modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PricingPlanListElement) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "description" in value:
        out["Description"] = value["description"]
    out["Size"] = value.get("size", 0)
    out["CreationTime"] = value.get("creation_time", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    return out


def deserialize_json(data: dict) -> PricingPlanListElement:
    out: PricingPlanListElement = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    else:
        out["creation_time"] = 0
    if "LastModifiedTime" in data:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    return out
