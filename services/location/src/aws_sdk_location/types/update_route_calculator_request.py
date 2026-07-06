"""Generated from Smithy shape ``com.amazonaws.location#UpdateRouteCalculatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_location.types.pricing_plan
    import aws_sdk_location.types.resource_description
    import aws_sdk_location.types.resource_name


class UpdateRouteCalculatorRequest(TypedDict, closed=True):
    calculator_name: "aws_sdk_location.types.resource_name.ResourceName"
    """<p>The name of the route calculator resource to update.</p>"""
    pricing_plan: NotRequired["aws_sdk_location.types.pricing_plan.PricingPlan"]
    """<p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>"""
    description: NotRequired[
        "aws_sdk_location.types.resource_description.ResourceDescription"
    ]
    """<p>Updates the description for the route calculator resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRouteCalculatorRequest) -> dict:
    out: dict = {}
    if "pricing_plan" in value:
        out["PricingPlan"] = value["pricing_plan"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_json(data: dict) -> UpdateRouteCalculatorRequest:
    out: UpdateRouteCalculatorRequest = {}  # type: ignore[typeddict-item]
    if "PricingPlan" in data:
        out["pricing_plan"] = data["PricingPlan"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
