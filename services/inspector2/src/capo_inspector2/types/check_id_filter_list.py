"""Generated from Smithy shape ``com.amazonaws.inspector2#CheckIdFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_string_filter

CheckIdFilterList: TypeAlias = list[
    "capo_inspector2.types.cis_string_filter.CisStringFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CheckIdFilterList) -> list:
    import capo_inspector2.types.cis_string_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_string_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CheckIdFilterList:
    import capo_inspector2.types.cis_string_filter

    out: CheckIdFilterList = []
    for item in data:
        out.append(capo_inspector2.types.cis_string_filter.deserialize_json(item))
    return out
