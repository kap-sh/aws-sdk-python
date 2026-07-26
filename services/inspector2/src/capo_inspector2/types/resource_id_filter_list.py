"""Generated from Smithy shape ``com.amazonaws.inspector2#ResourceIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_string_filter

ResourceIdFilterList: TypeAlias = list[
    "capo_inspector2.types.cis_string_filter.CisStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceIdFilterList) -> list:
    import capo_inspector2.types.cis_string_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceIdFilterList:
    import capo_inspector2.types.cis_string_filter

    out: ResourceIdFilterList = []
    for item in data:
        out.append(capo_inspector2.types.cis_string_filter.deserialize_json(item))
    return out
