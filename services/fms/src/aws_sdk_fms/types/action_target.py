"""Generated from Smithy shape ``com.amazonaws.fms#ActionTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fms.types.length_bounded_string
    import aws_sdk_fms.types.resource_id


class ActionTarget(TypedDict, closed=True):
    resource_id: NotRequired["aws_sdk_fms.types.resource_id.ResourceId"]
    """<p>The ID of the remediation target.</p>"""
    description: NotRequired[
        "aws_sdk_fms.types.length_bounded_string.LengthBoundedString"
    ]
    """<p>A description of the remediation action target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTarget) -> dict:
    out: dict = {}
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTarget:
    out: ActionTarget = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
