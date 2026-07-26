"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.group

GroupList: TypeAlias = list["capo_resource_groups.types.group.Group"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupList) -> list:
    import capo_resource_groups.types.group

    out: list = []
    for item in value:
        out.append(capo_resource_groups.types.group.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupList:
    import capo_resource_groups.types.group

    out: GroupList = []
    for item in data:
        out.append(capo_resource_groups.types.group.deserialize_json(item))
    return out
