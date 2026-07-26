"""Generated from Smithy shape ``com.amazonaws.connect#UserHierarchyGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group

UserHierarchyGroupList: TypeAlias = list[
    "capo_connect.types.hierarchy_group.HierarchyGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserHierarchyGroupList) -> list:
    import capo_connect.types.hierarchy_group

    out: list = []
    for item in value:
        out.append(capo_connect.types.hierarchy_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserHierarchyGroupList:
    import capo_connect.types.hierarchy_group

    out: UserHierarchyGroupList = []
    for item in data:
        out.append(capo_connect.types.hierarchy_group.deserialize_json(item))
    return out
