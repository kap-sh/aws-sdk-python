"""Generated from Smithy shape ``com.amazonaws.inspector2#CisResultStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_result_status_filter

CisResultStatusFilterList: TypeAlias = list[
    "capo_inspector2.types.cis_result_status_filter.CisResultStatusFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: CisResultStatusFilterList) -> list:
    import capo_inspector2.types.cis_result_status_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_result_status_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> CisResultStatusFilterList:
    import capo_inspector2.types.cis_result_status_filter

    out: CisResultStatusFilterList = []
    for item in data:
        out.append(
            capo_inspector2.types.cis_result_status_filter.deserialize_json(item)
        )
    return out
