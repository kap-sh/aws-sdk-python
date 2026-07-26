"""Generated from Smithy shape ``com.amazonaws.devopsguru#ResourceTypeFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.resource_type_filter

ResourceTypeFilters: TypeAlias = list[
    "capo_devops_guru.types.resource_type_filter.ResourceTypeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeFilters) -> list:
    import capo_devops_guru.types.resource_type_filter

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.resource_type_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceTypeFilters:
    import capo_devops_guru.types.resource_type_filter

    out: ResourceTypeFilters = []
    for item in data:
        out.append(capo_devops_guru.types.resource_type_filter.deserialize_json(item))
    return out
