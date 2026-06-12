"""Generated from Smithy shape ``com.amazonaws.iot#AddThingToThingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.override_dynamic_groups
    import aws_sdk_iot.types.thing_arn
    import aws_sdk_iot.types.thing_group_arn
    import aws_sdk_iot.types.thing_group_name
    import aws_sdk_iot.types.thing_name


class AddThingToThingGroupRequest(TypedDict):
    thing_group_name: NotRequired["aws_sdk_iot.types.thing_group_name.ThingGroupName"]
    """<p>The name of the group to which you are adding a thing.</p>"""
    thing_group_arn: NotRequired["aws_sdk_iot.types.thing_group_arn.ThingGroupArn"]
    """<p>The ARN of the group to which you are adding a thing.</p>"""
    thing_name: NotRequired["aws_sdk_iot.types.thing_name.ThingName"]
    """<p>The name of the thing to add to a group.</p>"""
    thing_arn: NotRequired["aws_sdk_iot.types.thing_arn.ThingArn"]
    """<p>The ARN of the thing to add to a group.</p>"""
    override_dynamic_groups: (
        "aws_sdk_iot.types.override_dynamic_groups.OverrideDynamicGroups"
    )
    """<p>Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddThingToThingGroupRequest) -> dict:
    out: dict = {}
    if "thing_group_name" in value:
        out["thingGroupName"] = value["thing_group_name"]
    if "thing_group_arn" in value:
        out["thingGroupArn"] = value["thing_group_arn"]
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_arn" in value:
        out["thingArn"] = value["thing_arn"]
    out["overrideDynamicGroups"] = value.get("override_dynamic_groups", False)
    return out


def deserialize_json(data: dict) -> AddThingToThingGroupRequest:
    out: AddThingToThingGroupRequest = {}  # type: ignore[typeddict-item]
    if "thingGroupName" in data:
        out["thing_group_name"] = data["thingGroupName"]
    if "thingGroupArn" in data:
        out["thing_group_arn"] = data["thingGroupArn"]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "thingArn" in data:
        out["thing_arn"] = data["thingArn"]
    if "overrideDynamicGroups" in data:
        out["override_dynamic_groups"] = data["overrideDynamicGroups"]
    else:
        out["override_dynamic_groups"] = False
    return out
