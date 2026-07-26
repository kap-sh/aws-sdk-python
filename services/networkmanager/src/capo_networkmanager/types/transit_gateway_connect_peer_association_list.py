"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayConnectPeerAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.transit_gateway_connect_peer_association

TransitGatewayConnectPeerAssociationList: TypeAlias = list[
    "capo_networkmanager.types.transit_gateway_connect_peer_association.TransitGatewayConnectPeerAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayConnectPeerAssociationList) -> list:
    import capo_networkmanager.types.transit_gateway_connect_peer_association

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.transit_gateway_connect_peer_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TransitGatewayConnectPeerAssociationList:
    import capo_networkmanager.types.transit_gateway_connect_peer_association

    out: TransitGatewayConnectPeerAssociationList = []
    for item in data:
        out.append(
            capo_networkmanager.types.transit_gateway_connect_peer_association.deserialize_json(
                item
            )
        )
    return out
