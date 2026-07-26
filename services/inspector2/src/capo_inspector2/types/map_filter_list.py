"""Generated from Smithy shape ``com.amazonaws.inspector2#MapFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.map_filter

MapFilterList: TypeAlias = list["capo_inspector2.types.map_filter.MapFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: MapFilterList) -> list:
    import capo_inspector2.types.map_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.map_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> MapFilterList:
    import capo_inspector2.types.map_filter

    out: MapFilterList = []
    for item in data:
        out.append(capo_inspector2.types.map_filter.deserialize_json(item))
    return out
