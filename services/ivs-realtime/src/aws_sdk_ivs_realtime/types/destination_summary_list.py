"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#DestinationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.destination_summary

DestinationSummaryList: TypeAlias = list[
    "aws_sdk_ivs_realtime.types.destination_summary.DestinationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationSummaryList) -> list:
    import aws_sdk_ivs_realtime.types.destination_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_ivs_realtime.types.destination_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationSummaryList:
    import aws_sdk_ivs_realtime.types.destination_summary

    out: DestinationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ivs_realtime.types.destination_summary.deserialize_json(item)
        )
    return out
