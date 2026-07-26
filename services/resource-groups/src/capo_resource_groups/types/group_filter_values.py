"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.group_filter_value

GroupFilterValues: TypeAlias = list[
    "capo_resource_groups.types.group_filter_value.GroupFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupFilterValues:
    return list(data)
