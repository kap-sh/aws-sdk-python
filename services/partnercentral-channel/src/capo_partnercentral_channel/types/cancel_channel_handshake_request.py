"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#CancelChannelHandshakeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_channel.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.channel_handshake_identifier


class CancelChannelHandshakeRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the handshake request.</p>"""
    identifier: "capo_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier"
    """<p>The unique identifier of the channel handshake to cancel.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelChannelHandshakeRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelChannelHandshakeRequest:
    out: CancelChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
    if "catalog" in data:
        out["catalog"] = data["catalog"]
    else:
        raise DeserializationError("CancelChannelHandshakeRequest.catalog required")
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("CancelChannelHandshakeRequest.identifier required")
    return out
