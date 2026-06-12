"""Generated from Smithy shape ``com.amazonaws.synthetics#GroupSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.group_arn
    import aws_sdk_synthetics.types.group_name
    import aws_sdk_synthetics.types.string


class GroupSummary(TypedDict):
    id: NotRequired["aws_sdk_synthetics.types.string.String"]
    """<p>The unique ID of the group.</p>"""
    name: NotRequired["aws_sdk_synthetics.types.group_name.GroupName"]
    """<p>The name of the group.</p>"""
    arn: NotRequired["aws_sdk_synthetics.types.group_arn.GroupArn"]
    """<p>The ARN of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> GroupSummary:
    out: GroupSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
