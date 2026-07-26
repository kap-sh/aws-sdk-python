"""Generated from Smithy shape ``com.amazonaws.inspector2#TargetStatusFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cis_target_status_filter

TargetStatusFilterList: TypeAlias = list[
    "capo_inspector2.types.cis_target_status_filter.CisTargetStatusFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetStatusFilterList) -> list:
    import capo_inspector2.types.cis_target_status_filter

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cis_target_status_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetStatusFilterList:
    import capo_inspector2.types.cis_target_status_filter

    out: TargetStatusFilterList = []
    for item in data:
        out.append(
            capo_inspector2.types.cis_target_status_filter.deserialize_json(item)
        )
    return out
