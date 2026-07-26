"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ResourceFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resource_groups.types.resource_filter_value

ResourceFilterValues: TypeAlias = list[
    "capo_resource_groups.types.resource_filter_value.ResourceFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceFilterValues:
    return list(data)
