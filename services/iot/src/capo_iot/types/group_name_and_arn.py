"""Generated from Smithy shape ``com.amazonaws.iot#GroupNameAndArn``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.thing_group_arn
    import capo_iot.types.thing_group_name


class GroupNameAndArn(TypedDict, closed=True):
    group_name: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>The group name.</p>"""
    group_arn: NotRequired["capo_iot.types.thing_group_arn.ThingGroupArn"]
    """<p>The group ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupNameAndArn) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "group_arn" in value:
        out["groupArn"] = value["group_arn"]
    return out


def deserialize_json(data: dict) -> GroupNameAndArn:
    out: GroupNameAndArn = {}  # type: ignore[typeddict-item]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "groupArn" in data:
        out["group_arn"] = data["groupArn"]
    return out
