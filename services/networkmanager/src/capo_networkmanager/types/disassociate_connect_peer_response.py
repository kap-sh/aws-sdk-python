"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateConnectPeerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.connect_peer_association


class DisassociateConnectPeerResponse(TypedDict, closed=True):
    connect_peer_association: NotRequired[
        "capo_networkmanager.types.connect_peer_association.ConnectPeerAssociation"
    ]
    """<p>Describes the Connect peer association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateConnectPeerResponse) -> dict:
    out: dict = {}
    if "connect_peer_association" in value:
        import capo_networkmanager.types.connect_peer_association

        out["ConnectPeerAssociation"] = (
            capo_networkmanager.types.connect_peer_association.serialize_json(
                value["connect_peer_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateConnectPeerResponse:
    out: DisassociateConnectPeerResponse = {}  # type: ignore[typeddict-item]
    if "ConnectPeerAssociation" in data:
        import capo_networkmanager.types.connect_peer_association

        out["connect_peer_association"] = (
            capo_networkmanager.types.connect_peer_association.deserialize_json(
                data["ConnectPeerAssociation"]
            )
        )
    return out
