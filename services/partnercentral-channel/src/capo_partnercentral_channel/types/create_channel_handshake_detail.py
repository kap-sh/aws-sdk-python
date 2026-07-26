"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CreateChannelHandshakeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.arn
    import capo_partnercentral_channel.types.channel_handshake_id


class CreateChannelHandshakeDetail(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_channel.types.channel_handshake_id.ChannelHandshakeId"
    ]
    """<p>The unique identifier of the created handshake.</p>"""
    arn: NotRequired["capo_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the created handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateChannelHandshakeDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateChannelHandshakeDetail:
    out: CreateChannelHandshakeDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
