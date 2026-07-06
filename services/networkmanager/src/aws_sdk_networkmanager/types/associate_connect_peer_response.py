"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateConnectPeerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_association


class AssociateConnectPeerResponse(TypedDict, closed=True):
    connect_peer_association: NotRequired[
        "aws_sdk_networkmanager.types.connect_peer_association.ConnectPeerAssociation"
    ]
    """<p>The response to the Connect peer request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateConnectPeerResponse) -> dict:
    out: dict = {}
    if "connect_peer_association" in value:
        import aws_sdk_networkmanager.types.connect_peer_association

        out["ConnectPeerAssociation"] = (
            aws_sdk_networkmanager.types.connect_peer_association.serialize_json(
                value["connect_peer_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateConnectPeerResponse:
    out: AssociateConnectPeerResponse = {}  # type: ignore[typeddict-item]
    if "ConnectPeerAssociation" in data:
        import aws_sdk_networkmanager.types.connect_peer_association

        out["connect_peer_association"] = (
            aws_sdk_networkmanager.types.connect_peer_association.deserialize_json(
                data["ConnectPeerAssociation"]
            )
        )
    return out
