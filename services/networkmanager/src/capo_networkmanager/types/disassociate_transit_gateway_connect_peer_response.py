"""Generated from Smithy shape ``com.amazonaws.networkmanager#DisassociateTransitGatewayConnectPeerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.transit_gateway_connect_peer_association


class DisassociateTransitGatewayConnectPeerResponse(TypedDict, closed=True):
    transit_gateway_connect_peer_association: NotRequired[
        "capo_networkmanager.types.transit_gateway_connect_peer_association.TransitGatewayConnectPeerAssociation"
    ]
    """<p>The transit gateway Connect peer association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateTransitGatewayConnectPeerResponse) -> dict:
    out: dict = {}
    if "transit_gateway_connect_peer_association" in value:
        import capo_networkmanager.types.transit_gateway_connect_peer_association

        out["TransitGatewayConnectPeerAssociation"] = (
            capo_networkmanager.types.transit_gateway_connect_peer_association.serialize_json(
                value["transit_gateway_connect_peer_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> DisassociateTransitGatewayConnectPeerResponse:
    out: DisassociateTransitGatewayConnectPeerResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayConnectPeerAssociation" in data:
        import capo_networkmanager.types.transit_gateway_connect_peer_association

        out["transit_gateway_connect_peer_association"] = (
            capo_networkmanager.types.transit_gateway_connect_peer_association.deserialize_json(
                data["TransitGatewayConnectPeerAssociation"]
            )
        )
    return out
