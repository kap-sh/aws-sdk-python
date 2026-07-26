"""Generated from Smithy shape ``com.amazonaws.iot#ThingGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.thing_group_name

ThingGroupList: TypeAlias = list["capo_iot.types.thing_group_name.ThingGroupName"]


# --- restJson1 ser/de ---
def serialize_json(value: ThingGroupList) -> list:
    return list(value)


def deserialize_json(data: list) -> ThingGroupList:
    return list(data)
