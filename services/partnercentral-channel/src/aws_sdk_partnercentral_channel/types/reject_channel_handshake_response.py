"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RejectChannelHandshakeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.reject_channel_handshake_detail


class RejectChannelHandshakeResponse(TypedDict, closed=True):
    channel_handshake_detail: NotRequired[
        "aws_sdk_partnercentral_channel.types.reject_channel_handshake_detail.RejectChannelHandshakeDetail"
    ]
    """<p>Details of the rejected channel handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectChannelHandshakeResponse) -> dict:
    out: dict = {}
    if "channel_handshake_detail" in value:
        import aws_sdk_partnercentral_channel.types.reject_channel_handshake_detail

        out["channelHandshakeDetail"] = (
            aws_sdk_partnercentral_channel.types.reject_channel_handshake_detail.serialize_aws_json_1_0(
                value["channel_handshake_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectChannelHandshakeResponse:
    out: RejectChannelHandshakeResponse = {}  # type: ignore[typeddict-item]
    if "channelHandshakeDetail" in data:
        import aws_sdk_partnercentral_channel.types.reject_channel_handshake_detail

        out["channel_handshake_detail"] = (
            aws_sdk_partnercentral_channel.types.reject_channel_handshake_detail.deserialize_aws_json_1_0(
                data["channelHandshakeDetail"]
            )
        )
    return out
