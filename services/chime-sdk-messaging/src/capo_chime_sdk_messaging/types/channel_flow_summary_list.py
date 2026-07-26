"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelFlowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.channel_flow_summary

ChannelFlowSummaryList: TypeAlias = list[
    "capo_chime_sdk_messaging.types.channel_flow_summary.ChannelFlowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelFlowSummaryList) -> list:
    import capo_chime_sdk_messaging.types.channel_flow_summary

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_messaging.types.channel_flow_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ChannelFlowSummaryList:
    import capo_chime_sdk_messaging.types.channel_flow_summary

    out: ChannelFlowSummaryList = []
    for item in data:
        out.append(
            capo_chime_sdk_messaging.types.channel_flow_summary.deserialize_json(item)
        )
    return out
