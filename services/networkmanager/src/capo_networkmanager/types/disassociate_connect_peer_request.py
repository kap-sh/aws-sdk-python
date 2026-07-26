"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateConnectPeerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_id
    import capo_networkmanager.types.global_network_id


class DisassociateConnectPeerRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""
    connect_peer_id: "capo_networkmanager.types.connect_peer_id.ConnectPeerId"
    """<p>The ID of the Connect peer to disassociate from a device.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateConnectPeerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateConnectPeerRequest:
    out: DisassociateConnectPeerRequest = {}  # type: ignore[typeddict-item]
    return out
