"""Generated from Smithy shape ``com.amazonaws.iot#CreateThingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.tag_list
    import aws_sdk_iot.types.thing_group_name
    import aws_sdk_iot.types.thing_group_properties


class CreateThingGroupRequest(TypedDict, closed=True):
    thing_group_name: "aws_sdk_iot.types.thing_group_name.ThingGroupName"
    """<p>The thing group name to create.</p>"""
    parent_group_name: NotRequired["aws_sdk_iot.types.thing_group_name.ThingGroupName"]
    """<p>The name of the parent thing group.</p>"""
    thing_group_properties: NotRequired[
        "aws_sdk_iot.types.thing_group_properties.ThingGroupProperties"
    ]
    """<p>The thing group properties.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the thing group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateThingGroupRequest) -> dict:
    out: dict = {}
    if "parent_group_name" in value:
        out["parentGroupName"] = value["parent_group_name"]
    if "thing_group_properties" in value:
        import aws_sdk_iot.types.thing_group_properties

        out["thingGroupProperties"] = (
            aws_sdk_iot.types.thing_group_properties.serialize_json(
                value["thing_group_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateThingGroupRequest:
    out: CreateThingGroupRequest = {}  # type: ignore[typeddict-item]
    if "parentGroupName" in data:
        out["parent_group_name"] = data["parentGroupName"]
    if "thingGroupProperties" in data:
        import aws_sdk_iot.types.thing_group_properties

        out["thing_group_properties"] = (
            aws_sdk_iot.types.thing_group_properties.deserialize_json(
                data["thingGroupProperties"]
            )
        )
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    return out
