"""Generated from Smithy shape ``com.amazonaws.fis#TargetResourceTypeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.target_resource_type_description
    import capo_fis.types.target_resource_type_id


class TargetResourceTypeSummary(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_fis.types.target_resource_type_id.TargetResourceTypeId"
    ]
    """<p>The resource type.</p>"""
    description: NotRequired[
        "capo_fis.types.target_resource_type_description.TargetResourceTypeDescription"
    ]
    """<p>A description of the resource type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TargetResourceTypeSummary) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> TargetResourceTypeSummary:
    out: TargetResourceTypeSummary = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "description" in data:
        out["description"] = data["description"]
    return out
