"""Generated from Smithy shape ``com.amazonaws.ssm#TargetPreview``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.integer
    import aws_sdk_ssm.types.string


class TargetPreview(TypedDict):
    count: "aws_sdk_ssm.types.integer.Integer"
    """<p>The number of resources of a certain type included in an execution preview.</p>"""
    target_type: NotRequired["aws_sdk_ssm.types.string.String"]
    """<p>A type of resource that was included in the execution preview.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetPreview) -> dict:
    out: dict = {}
    out["Count"] = value.get("count", 0)
    if "target_type" in value:
        out["TargetType"] = value["target_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetPreview:
    out: TargetPreview = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    else:
        out["count"] = 0
    if "TargetType" in data:
        out["target_type"] = data["TargetType"]
    return out
