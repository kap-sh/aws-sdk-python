"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceMapFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.resource_map_filter

ResourceMapFilterList: TypeAlias = list[
    "capo_inspector2.types.resource_map_filter.ResourceMapFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMapFilterList) -> list:
    import capo_inspector2.types.resource_map_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.resource_map_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceMapFilterList:
    import capo_inspector2.types.resource_map_filter

    out: ResourceMapFilterList = []
    for item in data:
        out.append(capo_inspector2.types.resource_map_filter.deserialize_json(item))
    return out
