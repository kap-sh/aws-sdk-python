"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#RejectChannelHandshakeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.catalog
    import aws_sdk_partnercentral_channel.types.channel_handshake_identifier


class RejectChannelHandshakeRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the handshake request.</p>"""
    identifier: "aws_sdk_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier"
    """<p>The unique identifier of the channel handshake to reject.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RejectChannelHandshakeRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RejectChannelHandshakeRequest:
    out: RejectChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("RejectChannelHandshakeRequest.catalog required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("RejectChannelHandshakeRequest.identifier required")
    return out
