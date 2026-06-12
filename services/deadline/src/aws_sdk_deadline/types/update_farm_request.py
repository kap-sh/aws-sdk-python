"""Generated from Smithy shape ``com.amazonaws.deadline#UpdateFarmRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.cost_scale_factor
    import aws_sdk_deadline.types.description
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.resource_name


class UpdateFarmRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID to update.</p>"""
    display_name: NotRequired["aws_sdk_deadline.types.resource_name.ResourceName"]
    """<p>The display name of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    description: NotRequired["aws_sdk_deadline.types.description.Description"]
    """<p>The description of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>"""
    cost_scale_factor: NotRequired[
        "aws_sdk_deadline.types.cost_scale_factor.CostScaleFactor"
    ]
    """<p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFarmRequest) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "cost_scale_factor" in value:
        out["costScaleFactor"] = value["cost_scale_factor"]
    return out


def deserialize_json(data: dict) -> UpdateFarmRequest:
    out: UpdateFarmRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "costScaleFactor" in data:
        out["cost_scale_factor"] = data["costScaleFactor"]
    return out
