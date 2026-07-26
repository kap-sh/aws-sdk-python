"""Generated from Smithy shape ``com.amazonaws.inspector2#CisNumberFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_number_filter

CisNumberFilterList: TypeAlias = list[
    "capo_inspector2.types.cis_number_filter.CisNumberFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisNumberFilterList) -> list:
    import capo_inspector2.types.cis_number_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_number_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisNumberFilterList:
    import capo_inspector2.types.cis_number_filter

    out: CisNumberFilterList = []
    for item in data:
        out.append(capo_inspector2.types.cis_number_filter.deserialize_json(item))
    return out
