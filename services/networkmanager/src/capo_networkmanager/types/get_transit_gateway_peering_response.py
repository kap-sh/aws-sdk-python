"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayPeeringResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.transit_gateway_peering


class GetTransitGatewayPeeringResponse(TypedDict, closed=True):
    transit_gateway_peering: NotRequired[
        "capo_networkmanager.types.transit_gateway_peering.TransitGatewayPeering"
    ]
    """<p>Returns information about a transit gateway peering. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayPeeringResponse) -> dict:
    out: dict = {}
    if "transit_gateway_peering" in value:
        import capo_networkmanager.types.transit_gateway_peering

        out["TransitGatewayPeering"] = (
            capo_networkmanager.types.transit_gateway_peering.serialize_json(
                value["transit_gateway_peering"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTransitGatewayPeeringResponse:
    out: GetTransitGatewayPeeringResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayPeering" in data:
        import capo_networkmanager.types.transit_gateway_peering

        out["transit_gateway_peering"] = (
            capo_networkmanager.types.transit_gateway_peering.deserialize_json(
                data["TransitGatewayPeering"]
            )
        )
    return out
