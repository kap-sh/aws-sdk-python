"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_filter

GroupFilterList: TypeAlias = list[
    "aws_sdk_resource_groups.types.group_filter.GroupFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupFilterList) -> list:
    import aws_sdk_resource_groups.types.group_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_resource_groups.types.group_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupFilterList:
    import aws_sdk_resource_groups.types.group_filter

    out: GroupFilterList = []
    for item in data:
        out.append(aws_sdk_resource_groups.types.group_filter.deserialize_json(item))
    return out
