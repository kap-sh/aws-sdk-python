"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdatePricingPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.pricing_plan_arn
    import aws_sdk_billingconductor.types.pricing_plan_description
    import aws_sdk_billingconductor.types.pricing_plan_name


class UpdatePricingPlanInput(TypedDict):
    arn: "aws_sdk_billingconductor.types.pricing_plan_arn.PricingPlanArn"
    """<p>The Amazon Resource Name (ARN) of the pricing plan that you're updating. </p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_name.PricingPlanName"
    ]
    """<p>The name of the pricing plan. The name must be unique to each pricing plan. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.pricing_plan_description.PricingPlanDescription"
    ]
    """<p>The description of the pricing plan. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePricingPlanInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdatePricingPlanInput:
    out: UpdatePricingPlanInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdatePricingPlanInput.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
