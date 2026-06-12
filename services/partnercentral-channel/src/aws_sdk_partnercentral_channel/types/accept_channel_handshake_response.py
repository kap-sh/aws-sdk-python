"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#AcceptChannelHandshakeResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.accept_channel_handshake_detail


class AcceptChannelHandshakeResponse(TypedDict):
    channel_handshake_detail: NotRequired[
        "aws_sdk_partnercentral_channel.types.accept_channel_handshake_detail.AcceptChannelHandshakeDetail"
    ]
    """<p>Details of the accepted channel handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptChannelHandshakeResponse) -> dict:
    out: dict = {}
    if "channel_handshake_detail" in value:
        import aws_sdk_partnercentral_channel.types.accept_channel_handshake_detail

        out["channelHandshakeDetail"] = (
            aws_sdk_partnercentral_channel.types.accept_channel_handshake_detail.serialize_aws_json_1_0(
                value["channel_handshake_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptChannelHandshakeResponse:
    out: AcceptChannelHandshakeResponse = {}  # type: ignore[typeddict-item]
    if "channelHandshakeDetail" in data:
        import aws_sdk_partnercentral_channel.types.accept_channel_handshake_detail

        out["channel_handshake_detail"] = (
            aws_sdk_partnercentral_channel.types.accept_channel_handshake_detail.deserialize_aws_json_1_0(
                data["channelHandshakeDetail"]
            )
        )
    return out
