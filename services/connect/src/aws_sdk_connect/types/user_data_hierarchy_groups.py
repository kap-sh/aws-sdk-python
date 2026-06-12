"""Generated from Smithy shape ``com.amazonaws.connect#UserDataHierarchyGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_id

UserDataHierarchyGroups: TypeAlias = list[
    "aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserDataHierarchyGroups) -> list:
    return list(value)


def deserialize_json(data: list) -> UserDataHierarchyGroups:
    return list(data)
