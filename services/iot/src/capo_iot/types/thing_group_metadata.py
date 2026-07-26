"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.creation_date
    import capo_iot.types.thing_group_name
    import capo_iot.types.thing_group_name_and_arn_list


class ThingGroupMetadata(TypedDict, closed=True):
    parent_group_name: NotRequired["capo_iot.types.thing_group_name.ThingGroupName"]
    """<p>The parent thing group name.</p>"""
    root_to_parent_thing_groups: NotRequired[
        "capo_iot.types.thing_group_name_and_arn_list.ThingGroupNameAndArnList"
    ]
    """<p>The root parent thing group.</p>"""
    creation_date: NotRequired["capo_iot.types.creation_date.CreationDate"]
    """<p>The UNIX timestamp of when the thing group was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupMetadata) -> dict:
    out: dict = {}
    if "parent_group_name" in value:
        out["parentGroupName"] = value["parent_group_name"]
    if "root_to_parent_thing_groups" in value:
        import capo_iot.types.thing_group_name_and_arn_list

        out["rootToParentThingGroups"] = (
            capo_iot.types.thing_group_name_and_arn_list.serialize_json(
                value["root_to_parent_thing_groups"]
            )
        )
    if "creation_date" in value:
        import capo_iot.types.creation_date

        out["creationDate"] = capo_iot.types.creation_date.serialize_json(
            value["creation_date"]
        )
    return out


def deserialize_json(data: dict) -> ThingGroupMetadata:
    out: ThingGroupMetadata = {}  # type: ignore[typeddict-item]
    if "parentGroupName" in data:
        out["parent_group_name"] = data["parentGroupName"]
    if "rootToParentThingGroups" in data:
        import capo_iot.types.thing_group_name_and_arn_list

        out["root_to_parent_thing_groups"] = (
            capo_iot.types.thing_group_name_and_arn_list.deserialize_json(
                data["rootToParentThingGroups"]
            )
        )
    if "creationDate" in data:
        import capo_iot.types.creation_date

        out["creation_date"] = capo_iot.types.creation_date.deserialize_json(
            data["creationDate"]
        )
    return out
