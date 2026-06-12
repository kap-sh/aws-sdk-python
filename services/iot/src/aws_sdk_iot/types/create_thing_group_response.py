"""Generated from Smithy shape ``com.amazonaws.iot#CreateThingGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.thing_group_arn
    import aws_sdk_iot.types.thing_group_id
    import aws_sdk_iot.types.thing_group_name


class CreateThingGroupResponse(TypedDict):
    thing_group_name: NotRequired["aws_sdk_iot.types.thing_group_name.ThingGroupName"]
    """<p>The thing group name.</p>"""
    thing_group_arn: NotRequired["aws_sdk_iot.types.thing_group_arn.ThingGroupArn"]
    """<p>The thing group ARN.</p>"""
    thing_group_id: NotRequired["aws_sdk_iot.types.thing_group_id.ThingGroupId"]
    """<p>The thing group ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThingGroupResponse) -> dict:
    out: dict = {}
    if "thing_group_name" in value:
        out["thingGroupName"] = value["thing_group_name"]
    if "thing_group_arn" in value:
        out["thingGroupArn"] = value["thing_group_arn"]
    if "thing_group_id" in value:
        out["thingGroupId"] = value["thing_group_id"]
    return out


def deserialize_json(data: dict) -> CreateThingGroupResponse:
    out: CreateThingGroupResponse = {}  # type: ignore[typeddict-item]
    if "thingGroupName" in data:
        out["thing_group_name"] = data["thingGroupName"]
    if "thingGroupArn" in data:
        out["thing_group_arn"] = data["thingGroupArn"]
    if "thingGroupId" in data:
        out["thing_group_id"] = data["thingGroupId"]
    return out
