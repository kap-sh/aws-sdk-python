"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupDocument``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.attributes
    import capo_iot.types.thing_group_description
    import capo_iot.types.thing_group_id
    import capo_iot.types.thing_group_name
    import capo_iot.types.thing_group_name_list


class ThingGroupDocument(TypedDict, closed=True):
    thing_group_name: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>The thing group name.</p>"""
    thing_group_id: NotRequired["capo_iot.types.thing_group_id.ThingGroupId"]
    """<p>The thing group ID.</p>"""
    thing_group_description: NotRequired[
        "capo_iot.types.thing_group_description.ThingGroupDescription"
    ]
    """<p>The thing group description.</p>"""
    attributes: NotRequired["capo_iot.types.attributes.Attributes"]
    """<p>The thing group attributes.</p>"""
    parent_group_names: NotRequired[
        "capo_iot.types.thing_group_name_list.ThingGroupNameList"
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
        import capo_iot.types.attributes

        out["attributes"] = capo_iot.types.attributes.serialize_json(
            value["attributes"]
        )
    if "parent_group_names" in value:
        import capo_iot.types.thing_group_name_list

        out["parentGroupNames"] = capo_iot.types.thing_group_name_list.serialize_json(
            value["parent_group_names"]
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
        import capo_iot.types.attributes

        out["attributes"] = capo_iot.types.attributes.deserialize_json(
            data["attributes"]
        )
    if "parentGroupNames" in data:
        import capo_iot.types.thing_group_name_list

        out["parent_group_names"] = (
            capo_iot.types.thing_group_name_list.deserialize_json(
                data["parentGroupNames"]
            )
        )
    return out
