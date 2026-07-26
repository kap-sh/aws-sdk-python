"""Generated from Smithy shape ``com.amazonaws.quicksight#VPCConnectionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.vpc_connection_summary

VPCConnectionSummaryList: TypeAlias = list[
    "capo_quicksight.types.vpc_connection_summary.VPCConnectionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: VPCConnectionSummaryList) -> list:
    import capo_quicksight.types.vpc_connection_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.vpc_connection_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> VPCConnectionSummaryList:
    import capo_quicksight.types.vpc_connection_summary

    out: VPCConnectionSummaryList = []
    for item in data:
        out.append(capo_quicksight.types.vpc_connection_summary.deserialize_json(item))
    return out
