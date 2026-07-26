"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceStringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.resource_string_filter

ResourceStringFilterList: TypeAlias = list[
    "capo_inspector2.types.resource_string_filter.ResourceStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStringFilterList) -> list:
    import capo_inspector2.types.resource_string_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.resource_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceStringFilterList:
    import capo_inspector2.types.resource_string_filter

    out: ResourceStringFilterList = []
    for item in data:
        out.append(capo_inspector2.types.resource_string_filter.deserialize_json(item))
    return out
