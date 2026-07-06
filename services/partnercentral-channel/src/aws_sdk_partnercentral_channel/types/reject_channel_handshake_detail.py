"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RejectChannelHandshakeDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.arn
    import aws_sdk_partnercentral_channel.types.channel_handshake_id
    import aws_sdk_partnercentral_channel.types.handshake_status


class RejectChannelHandshakeDetail(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_partnercentral_channel.types.channel_handshake_id.ChannelHandshakeId"
    ]
    """<p>The unique identifier of the rejected handshake.</p>"""
    arn: NotRequired["aws_sdk_partnercentral_channel.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the rejected handshake.</p>"""
    status: NotRequired[
        "aws_sdk_partnercentral_channel.types.handshake_status.HandshakeStatus"
    ]
    """<p>The current status of the rejected handshake.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectChannelHandshakeDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "status" in value:
        import aws_sdk_partnercentral_channel.types.handshake_status

        out["status"] = (
            aws_sdk_partnercentral_channel.types.handshake_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectChannelHandshakeDetail:
    out: RejectChannelHandshakeDetail = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "status" in data:
        import aws_sdk_partnercentral_channel.types.handshake_status

        out["status"] = (
            aws_sdk_partnercentral_channel.types.handshake_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    return out
