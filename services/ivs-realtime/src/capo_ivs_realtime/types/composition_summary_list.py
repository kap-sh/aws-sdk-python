"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CompositionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.composition_summary

CompositionSummaryList: TypeAlias = list[
    "capo_ivs_realtime.types.composition_summary.CompositionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositionSummaryList) -> list:
    import capo_ivs_realtime.types.composition_summary

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.composition_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CompositionSummaryList:
    import capo_ivs_realtime.types.composition_summary

    out: CompositionSummaryList = []
    for item in data:
        out.append(capo_ivs_realtime.types.composition_summary.deserialize_json(item))
    return out
