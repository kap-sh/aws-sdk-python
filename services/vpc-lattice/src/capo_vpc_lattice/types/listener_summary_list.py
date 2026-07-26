"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListenerSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.listener_summary

ListenerSummaryList: TypeAlias = list[
    "capo_vpc_lattice.types.listener_summary.ListenerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListenerSummaryList) -> list:
    import capo_vpc_lattice.types.listener_summary

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.listener_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListenerSummaryList:
    import capo_vpc_lattice.types.listener_summary

    out: ListenerSummaryList = []
    for item in data:
        out.append(capo_vpc_lattice.types.listener_summary.deserialize_json(item))
    return out
