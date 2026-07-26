"""Generated from Smithy shape ``com.amazonaws.inspector2#CisScanDateFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_date_filter

CisScanDateFilterList: TypeAlias = list[
    "capo_inspector2.types.cis_date_filter.CisDateFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisScanDateFilterList) -> list:
    import capo_inspector2.types.cis_date_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_date_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisScanDateFilterList:
    import capo_inspector2.types.cis_date_filter

    out: CisScanDateFilterList = []
    for item in data:
        out.append(capo_inspector2.types.cis_date_filter.deserialize_json(item))
    return out
