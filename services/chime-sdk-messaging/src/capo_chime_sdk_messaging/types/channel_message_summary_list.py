"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMessageSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_message_summary

ChannelMessageSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_message_summary.ChannelMessageSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMessageSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_message_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.channel_message_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChannelMessageSummaryList:
    import capo_chime_sdk_messaging.types.channel_message_summary

    out: ChannelMessageSummaryList = []
    for item in data:
        out.append(
            capo_chime_sdk_messaging.types.channel_message_summary.deserialize_json(
                item
            )
        )
    return out
