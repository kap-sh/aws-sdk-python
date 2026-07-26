"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.target_summary

TargetSummaryList: TypeAlias = list[
    "capo_vpc_lattice.types.target_summary.TargetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetSummaryList) -> list:
    import capo_vpc_lattice.types.target_summary

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.target_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetSummaryList:
    import capo_vpc_lattice.types.target_summary

    out: TargetSummaryList = []
    for item in data:
        out.append(capo_vpc_lattice.types.target_summary.deserialize_json(item))
    return out
