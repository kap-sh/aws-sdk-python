"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetGroupInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_name
    import capo_resource_groups.types.group_string_v2


class GetGroupInput(TypedDict, closed=True):
    group_name: NotRequired["capo_resource_groups.types.group_name.GroupName"]
    """<p>Deprecated - don't use this parameter. Use <code>Group</code> instead.</p>"""
    group: NotRequired["capo_resource_groups.types.group_string_v2.GroupStringV2"]
    """<p>The name or the Amazon resource name (ARN) of the resource group to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupInput) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group" in value:
        out["Group"] = value["group"]
    return out


def deserialize_json(data: dict) -> GetGroupInput:
    out: GetGroupInput = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "Group" in data:
        out["group"] = data["Group"]
    return out
