"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ChannelHandshakeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.channel_handshake_summary

ChannelHandshakeSummaries: TypeAlias = list[
    "capo_partnercentral_channel.types.channel_handshake_summary.ChannelHandshakeSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ChannelHandshakeSummaries) -> list:
    import capo_partnercentral_channel.types.channel_handshake_summary

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_channel.types.channel_handshake_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ChannelHandshakeSummaries:
    import capo_partnercentral_channel.types.channel_handshake_summary

    out: ChannelHandshakeSummaries = []
    for item in data:
        out.append(
            capo_partnercentral_channel.types.channel_handshake_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
