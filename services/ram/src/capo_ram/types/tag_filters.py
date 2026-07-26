"""Generated from Smithy shape ``com.amazonaws.ram#TagFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ram.types.tag_filter

TagFilters: TypeAlias = list["capo_ram.types.tag_filter.TagFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: TagFilters) -> list:
    import capo_ram.types.tag_filter

    out: list = []
    for item in value:
        out.append(capo_ram.types.tag_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagFilters:
    import capo_ram.types.tag_filter

    out: TagFilters = []
    for item in data:
        out.append(capo_ram.types.tag_filter.deserialize_json(item))
    return out
