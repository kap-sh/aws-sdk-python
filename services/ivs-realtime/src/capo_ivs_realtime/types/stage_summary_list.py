"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ivs_realtime.types.stage_summary

StageSummaryList: TypeAlias = list["capo_ivs_realtime.types.stage_summary.StageSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: StageSummaryList) -> list:
    import capo_ivs_realtime.types.stage_summary

    out: list = []
    for item in value:
        out.append(capo_ivs_realtime.types.stage_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StageSummaryList:
    import capo_ivs_realtime.types.stage_summary

    out: StageSummaryList = []
    for item in data:
        out.append(capo_ivs_realtime.types.stage_summary.deserialize_json(item))
    return out
