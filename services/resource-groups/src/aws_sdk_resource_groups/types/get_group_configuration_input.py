"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GetGroupConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_string


class GetGroupConfigurationInput(TypedDict, closed=True):
    group: NotRequired["aws_sdk_resource_groups.types.group_string.GroupString"]
    """<p>The name or the Amazon resource name (ARN) of the resource group for which you want to retrive the service configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupConfigurationInput) -> dict:
    out: dict = {}
    if "group" in value:
        out["Group"] = value["group"]
    return out


def deserialize_json(data: dict) -> GetGroupConfigurationInput:
    out: GetGroupConfigurationInput = {}  # type: ignore[typeddict-item]
    if "Group" in data:
        out["group"] = data["Group"]
    return out
