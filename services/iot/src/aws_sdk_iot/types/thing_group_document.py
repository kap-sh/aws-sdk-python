"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.attributes
    import aws_sdk_iot.types.thing_group_description
    import aws_sdk_iot.types.thing_group_id
    import aws_sdk_iot.types.thing_group_name
    import aws_sdk_iot.types.thing_group_name_list


class ThingGroupDocument(TypedDict, closed=True):
    thing_group_name: NotRequired["aws_sdk_iot.types.thing_group_name.ThingGroupName"]
    """<p>The thing group name.</p>"""
    thing_group_id: NotRequired["aws_sdk_iot.types.thing_group_id.ThingGroupId"]
    """<p>The thing group ID.</p>"""
    thing_group_description: NotRequired[
        "aws_sdk_iot.types.thing_group_description.ThingGroupDescription"
    ]
    """<p>The thing group description.</p>"""
    attributes: NotRequired["aws_sdk_iot.types.attributes.Attributes"]
    """<p>The thing group attributes.</p>"""
    parent_group_names: NotRequired[
        "aws_sdk_iot.types.thing_group_name_list.ThingGroupNameList"
    ]
    """<p>Parent group names.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupDocument) -> dict:
    out: dict = {}
    if "thing_group_name" in value:
        out["thingGroupName"] = value["thing_group_name"]
    if "thing_group_id" in value:
        out["thingGroupId"] = value["thing_group_id"]
    if "thing_group_description" in value:
        out["thingGroupDescription"] = value["thing_group_description"]
    if "attributes" in value:
        import aws_sdk_iot.types.attributes

        out["attributes"] = aws_sdk_iot.types.attributes.serialize_json(
            value["attributes"]
        )
    if "parent_group_names" in value:
        import aws_sdk_iot.types.thing_group_name_list

        out["parentGroupNames"] = (
            aws_sdk_iot.types.thing_group_name_list.serialize_json(
                value["parent_group_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> ThingGroupDocument:
    out: ThingGroupDocument = {}  # type: ignore[typeddict-item]
    if "thingGroupName" in data:
        out["thing_group_name"] = data["thingGroupName"]
    if "thingGroupId" in data:
        out["thing_group_id"] = data["thingGroupId"]
    if "thingGroupDescription" in data:
        out["thing_group_description"] = data["thingGroupDescription"]
    if "attributes" in data:
        import aws_sdk_iot.types.attributes

        out["attributes"] = aws_sdk_iot.types.attributes.deserialize_json(
            data["attributes"]
        )
    if "parentGroupNames" in data:
        import aws_sdk_iot.types.thing_group_name_list

        out["parent_group_names"] = (
            aws_sdk_iot.types.thing_group_name_list.deserialize_json(
                data["parentGroupNames"]
            )
        )
    return out
