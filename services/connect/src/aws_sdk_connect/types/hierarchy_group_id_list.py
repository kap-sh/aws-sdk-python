"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroupIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_id

HierarchyGroupIdList: TypeAlias = list[
    "aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroupIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> HierarchyGroupIdList:
    return list(data)
