"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.destination_summary

DestinationSummaryList: TypeAlias = list[
    "capo_ivs_realtime.types.destination_summary.DestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationSummaryList) -> list:
    import capo_ivs_realtime.types.destination_summary

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.destination_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationSummaryList:
    import capo_ivs_realtime.types.destination_summary

    out: DestinationSummaryList = []
    for item in data:
        out.append(capo_ivs_realtime.types.destination_summary.deserialize_json(item))
    return out
