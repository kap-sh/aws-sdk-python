"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayConnectPeerAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.next_token
    import capo_networkmanager.types.transit_gateway_connect_peer_association_list


class GetTransitGatewayConnectPeerAssociationsResponse(TypedDict, closed=True):
    transit_gateway_connect_peer_associations: NotRequired[
        "capo_networkmanager.types.transit_gateway_connect_peer_association_list.TransitGatewayConnectPeerAssociationList"
    ]
    """<p>Information about the transit gateway Connect peer associations.</p>"""
    next_token: NotRequired["capo_networkmanager.types.next_token.NextToken"]
    """<p>The token to use for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayConnectPeerAssociationsResponse) -> dict:
    out: dict = {}
    if "transit_gateway_connect_peer_associations" in value:
        import capo_networkmanager.types.transit_gateway_connect_peer_association_list

        out["TransitGatewayConnectPeerAssociations"] = (
            capo_networkmanager.types.transit_gateway_connect_peer_association_list.serialize_json(
                value["transit_gateway_connect_peer_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetTransitGatewayConnectPeerAssociationsResponse:
    out: GetTransitGatewayConnectPeerAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayConnectPeerAssociations" in data:
        import capo_networkmanager.types.transit_gateway_connect_peer_association_list

        out["transit_gateway_connect_peer_associations"] = (
            capo_networkmanager.types.transit_gateway_connect_peer_association_list.deserialize_json(
                data["TransitGatewayConnectPeerAssociations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
