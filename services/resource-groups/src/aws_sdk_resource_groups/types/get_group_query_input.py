"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetGroupQueryInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_name
    import aws_sdk_resource_groups.types.group_string


class GetGroupQueryInput(TypedDict):
    group_name: NotRequired["aws_sdk_resource_groups.types.group_name.GroupName"]
    """<p>Don't use this parameter. Use <code>Group</code> instead.</p>"""
    group: NotRequired["aws_sdk_resource_groups.types.group_string.GroupString"]
    """<p>The name or the Amazon resource name (ARN) of the resource group to query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupQueryInput) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group" in value:
        out["Group"] = value["group"]
    return out


def deserialize_json(data: dict) -> GetGroupQueryInput:
    out: GetGroupQueryInput = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "Group" in data:
        out["group"] = data["Group"]
    return out
