"""Generated from Smithy shape ``com.amazonaws.fis#ActionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.target_resource_type_id


class ActionTarget(TypedDict, closed=True):
    resource_type: NotRequired[
        "aws_sdk_fis.types.target_resource_type_id.TargetResourceTypeId"
    ]
    """<p>The resource type of the target.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionTarget) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> ActionTarget:
    out: ActionTarget = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    return out
