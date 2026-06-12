"""Generated from Smithy shape ``com.amazonaws.iot#RemoveThingFromThingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_arn
    import aws_sdk_iot.types.thing_group_arn
    import aws_sdk_iot.types.thing_group_name
    import aws_sdk_iot.types.thing_name


class RemoveThingFromThingGroupRequest(TypedDict):
    thing_group_name: NotRequired["aws_sdk_iot.types.thing_group_name.ThingGroupName"]
    """<p>The group name.</p>"""
    thing_group_arn: NotRequired["aws_sdk_iot.types.thing_group_arn.ThingGroupArn"]
    """<p>The group ARN.</p>"""
    thing_name: NotRequired["aws_sdk_iot.types.thing_name.ThingName"]
    """<p>The name of the thing to remove from the group.</p>"""
    thing_arn: NotRequired["aws_sdk_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing to remove from the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RemoveThingFromThingGroupRequest) -> dict:
    out: dict = {}
    if "thing_group_name" in value:
        out["thingGroupName"] = value["thing_group_name"]
    if "thing_group_arn" in value:
        out["thingGroupArn"] = value["thing_group_arn"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    return out


def deserialize_json(data: dict) -> RemoveThingFromThingGroupRequest:
    out: RemoveThingFromThingGroupRequest = {}  # type: ignore[typeddict-item]
    if "thingGroupName" in data:
        out["thing_group_name"] = data["thingGroupName"]
    if "thingGroupArn" in data:
        out["thing_group_arn"] = data["thingGroupArn"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    return out
