"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#SubChannelSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.sub_channel_summary

SubChannelSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.sub_channel_summary.SubChannelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SubChannelSummaryList) -> list:
    import capo_chime_sdk_messaging.types.sub_channel_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.sub_channel_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SubChannelSummaryList:
    import capo_chime_sdk_messaging.types.sub_channel_summary

    out: SubChannelSummaryList = []
    for item in data:
        out.append(
            capo_chime_sdk_messaging.types.sub_channel_summary.deserialize_json(item)
        )
    return out
