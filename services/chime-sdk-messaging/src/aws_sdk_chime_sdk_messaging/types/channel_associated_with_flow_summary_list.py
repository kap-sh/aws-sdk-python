"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelAssociatedWithFlowSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary

ChannelAssociatedWithFlowSummaryList: TypeAlias = list[
    "aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary.ChannelAssociatedWithFlowSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelAssociatedWithFlowSummaryList) -> list:
    import aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelAssociatedWithFlowSummaryList:
    import aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary

    out: ChannelAssociatedWithFlowSummaryList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_messaging.types.channel_associated_with_flow_summary.deserialize_json(
                item
            )
        )
    return out
