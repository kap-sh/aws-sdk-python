"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#CompositionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.composition_summary

CompositionSummaryList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.composition_summary.CompositionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CompositionSummaryList) -> list:
    import aws_sdk_ivs_realtime.types.composition_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs_realtime.types.composition_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> CompositionSummaryList:
    import aws_sdk_ivs_realtime.types.composition_summary

    out: CompositionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.composition_summary.deserialize_json(item)
        )
    return out
