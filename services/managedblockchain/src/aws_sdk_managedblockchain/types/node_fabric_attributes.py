"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NodeFabricAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.string


class NodeFabricAttributes(TypedDict, closed=True):
    peer_endpoint: NotRequired["aws_sdk_managedblockchain.types.string.String"]
    """<p>The endpoint that identifies the peer node for all services except peer channel-based event services.</p>"""
    peer_event_endpoint: NotRequired["aws_sdk_managedblockchain.types.string.String"]
    """<p>The endpoint that identifies the peer node for peer channel-based event services.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeFabricAttributes) -> dict:
    out: dict = {}
    if "peer_endpoint" in value:
        out["PeerEndpoint"] = value["peer_endpoint"]
    if "peer_event_endpoint" in value:
        out["PeerEventEndpoint"] = value["peer_event_endpoint"]
    return out


def deserialize_json(data: dict) -> NodeFabricAttributes:
    out: NodeFabricAttributes = {}  # type: ignore[typeddict-item]
    if "PeerEndpoint" in data:
        out["peer_endpoint"] = data["PeerEndpoint"]
    if "PeerEventEndpoint" in data:
        out["peer_event_endpoint"] = data["PeerEventEndpoint"]
    return out
