"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#ChannelMembershipSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_summary

ChannelMembershipSummaryList: TypeAlias = list[
    "aws_sdk_chime_sdk_messaging.types.channel_membership_summary.ChannelMembershipSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelMembershipSummaryList) -> list:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_messaging.types.channel_membership_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ChannelMembershipSummaryList:
    import aws_sdk_chime_sdk_messaging.types.channel_membership_summary

    out: ChannelMembershipSummaryList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_messaging.types.channel_membership_summary.deserialize_json(
                item
            )
        )
    return out
