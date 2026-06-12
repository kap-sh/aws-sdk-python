"""Generated from Smithy shape ``com.amazonaws.iot#UpdateThingGroupsForThingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.override_dynamic_groups
    import aws_sdk_iot.types.thing_group_list
    import aws_sdk_iot.types.thing_name


class UpdateThingGroupsForThingRequest(TypedDict):
    thing_name: NotRequired["aws_sdk_iot.types.thing_name.ThingName"]
    """<p>The thing whose group memberships will be updated.</p>"""
    thing_groups_to_add: NotRequired[
        "aws_sdk_iot.types.thing_group_list.ThingGroupList"
    ]
    """<p>The groups to which the thing will be added.</p>"""
    thing_groups_to_remove: NotRequired[
        "aws_sdk_iot.types.thing_group_list.ThingGroupList"
    ]
    """<p>The groups from which the thing will be removed.</p>"""
    override_dynamic_groups: (
        "aws_sdk_iot.types.override_dynamic_groups.OverrideDynamicGroups"
    )
    """<p>Override dynamic thing groups with static thing groups when 10-group limit is reached. If a thing belongs to 10 thing groups, and one or more of those groups are dynamic thing groups, adding a thing to a static group removes the thing from the last dynamic group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThingGroupsForThingRequest) -> dict:
    out: dict = {}
    if "thing_name" in value:
        out["thingName"] = value["thing_name"]
    if "thing_groups_to_add" in value:
        import aws_sdk_iot.types.thing_group_list

        out["thingGroupsToAdd"] = aws_sdk_iot.types.thing_group_list.serialize_json(
            value["thing_groups_to_add"]
        )
    if "thing_groups_to_remove" in value:
        import aws_sdk_iot.types.thing_group_list

        out["thingGroupsToRemove"] = aws_sdk_iot.types.thing_group_list.serialize_json(
            value["thing_groups_to_remove"]
        )
    out["overrideDynamicGroups"] = value.get("override_dynamic_groups", False)
    return out


def deserialize_json(data: dict) -> UpdateThingGroupsForThingRequest:
    out: UpdateThingGroupsForThingRequest = {}  # type: ignore[typeddict-item]
    if "thingName" in data:
        out["thing_name"] = data["thingName"]
    if "thingGroupsToAdd" in data:
        import aws_sdk_iot.types.thing_group_list

        out["thing_groups_to_add"] = (
            aws_sdk_iot.types.thing_group_list.deserialize_json(
                data["thingGroupsToAdd"]
            )
        )
    if "thingGroupsToRemove" in data:
        import aws_sdk_iot.types.thing_group_list

        out["thing_groups_to_remove"] = (
            aws_sdk_iot.types.thing_group_list.deserialize_json(
                data["thingGroupsToRemove"]
            )
        )
    if "overrideDynamicGroups" in data:
        out["override_dynamic_groups"] = data["overrideDynamicGroups"]
    else:
        out["override_dynamic_groups"] = False
    return out
