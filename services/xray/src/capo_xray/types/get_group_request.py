"""Generated from Smithy shape ``com.amazonaws.xray#GetGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.group_arn
    import capo_xray.types.group_name


class GetGroupRequest(TypedDict, closed=True):
    group_name: NotRequired["capo_xray.types.group_name.GroupName"]
    """<p>The case-sensitive name of the group.</p>"""
    group_arn: NotRequired["capo_xray.types.group_arn.GroupARN"]
    """<p>The ARN of the group that was generated on creation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGroupRequest) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_arn" in value:
        out["GroupARN"] = value["group_arn"]
    return out


def deserialize_json(data: dict) -> GetGroupRequest:
    out: GetGroupRequest = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupARN" in data:
        out["group_arn"] = data["GroupARN"]
    return out
