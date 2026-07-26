"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#AcceptChannelHandshakeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.arn
    import capo_partnercentral_channel.types.channel_handshake_id
    import capo_partnercentral_channel.types.handshake_status


class AcceptChannelHandshakeDetail(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_channel.types.channel_handshake_id.ChannelHandshakeId"
    ]
    """<p>The unique identifier of the accepted handshake.</p>"""
    arn: NotRequired["capo_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the accepted handshake.</p>"""
    status: NotRequired[
        "capo_partnercentral_channel.types.handshake_status.HandshakeStatus"
    ]
    """<p>The current status of the accepted handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptChannelHandshakeDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import capo_partnercentral_channel.types.handshake_status

        out["status"] = (
            capo_partnercentral_channel.types.handshake_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptChannelHandshakeDetail:
    out: AcceptChannelHandshakeDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import capo_partnercentral_channel.types.handshake_status

        out["status"] = (
            capo_partnercentral_channel.types.handshake_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
