"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateChannelHandshakeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.create_channel_handshake_detail


class CreateChannelHandshakeResponse(TypedDict, closed=True):
    channel_handshake_detail: NotRequired[
        "capo_partnercentral_channel.types.create_channel_handshake_detail.CreateChannelHandshakeDetail"
    ]
    """<p>Details of the created channel handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateChannelHandshakeResponse) -> dict:
    out: dict = {}
    if "channel_handshake_detail" in value:
        import capo_partnercentral_channel.types.create_channel_handshake_detail

        out["channelHandshakeDetail"] = (
            capo_partnercentral_channel.types.create_channel_handshake_detail.serialize_aws_json_1_0(
                value["channel_handshake_detail"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateChannelHandshakeResponse:
    out: CreateChannelHandshakeResponse = {}  # type: ignore[typeddict-item]
    if "channelHandshakeDetail" in data:
        import capo_partnercentral_channel.types.create_channel_handshake_detail

        out["channel_handshake_detail"] = (
            capo_partnercentral_channel.types.create_channel_handshake_detail.deserialize_aws_json_1_0(
                data["channelHandshakeDetail"]
            )
        )
    return out
