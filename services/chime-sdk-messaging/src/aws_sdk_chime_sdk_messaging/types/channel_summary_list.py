"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_summary

ChannelSummaryList: TypeAlias = list[
    "aws_sdk_chime_sdk_messaging.types.channel_summary.ChannelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelSummaryList) -> list:
    import aws_sdk_chime_sdk_messaging.types.channel_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_messaging.types.channel_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChannelSummaryList:
    import aws_sdk_chime_sdk_messaging.types.channel_summary

    out: ChannelSummaryList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_messaging.types.channel_summary.deserialize_json(item)
        )
    return out
