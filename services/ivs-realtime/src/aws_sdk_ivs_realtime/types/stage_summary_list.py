"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage_summary

StageSummaryList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.stage_summary.StageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: StageSummaryList) -> list:
    import aws_sdk_ivs_realtime.types.stage_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs_realtime.types.stage_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> StageSummaryList:
    import aws_sdk_ivs_realtime.types.stage_summary

    out: StageSummaryList = []
    for item in data:
        out.append(aws_sdk_ivs_realtime.types.stage_summary.deserialize_json(item))
    return out
