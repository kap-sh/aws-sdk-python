"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SubChannelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.sub_channel_summary

SubChannelSummaryList: TypeAlias = list[
    "aws_sdk_chime_sdk_messaging.types.sub_channel_summary.SubChannelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubChannelSummaryList) -> list:
    import aws_sdk_chime_sdk_messaging.types.sub_channel_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_messaging.types.sub_channel_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubChannelSummaryList:
    import aws_sdk_chime_sdk_messaging.types.sub_channel_summary

    out: SubChannelSummaryList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_messaging.types.sub_channel_summary.deserialize_json(item)
        )
    return out
