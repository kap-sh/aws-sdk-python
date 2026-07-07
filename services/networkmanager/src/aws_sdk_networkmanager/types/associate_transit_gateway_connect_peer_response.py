"""Generated from Smithy shape ``com.amazonaws.networkmanager#AssociateTransitGatewayConnectPeerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.transit_gateway_connect_peer_association


class AssociateTransitGatewayConnectPeerResponse(TypedDict, closed=True):
    transit_gateway_connect_peer_association: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_connect_peer_association.TransitGatewayConnectPeerAssociation"
    ]
    """<p>The transit gateway Connect peer association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateTransitGatewayConnectPeerResponse) -> dict:
    out: dict = {}
    if "transit_gateway_connect_peer_association" in value:
        import aws_sdk_networkmanager.types.transit_gateway_connect_peer_association

        out["TransitGatewayConnectPeerAssociation"] = (
            aws_sdk_networkmanager.types.transit_gateway_connect_peer_association.serialize_json(
                value["transit_gateway_connect_peer_association"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateTransitGatewayConnectPeerResponse:
    out: AssociateTransitGatewayConnectPeerResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayConnectPeerAssociation" in data:
        import aws_sdk_networkmanager.types.transit_gateway_connect_peer_association

        out["transit_gateway_connect_peer_association"] = (
            aws_sdk_networkmanager.types.transit_gateway_connect_peer_association.deserialize_json(
                data["TransitGatewayConnectPeerAssociation"]
            )
        )
    return out
