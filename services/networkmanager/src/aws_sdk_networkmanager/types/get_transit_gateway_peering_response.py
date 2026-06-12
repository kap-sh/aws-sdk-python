"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayPeeringResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.transit_gateway_peering


class GetTransitGatewayPeeringResponse(TypedDict):
    transit_gateway_peering: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_peering.TransitGatewayPeering"
    ]
    """<p>Returns information about a transit gateway peering. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayPeeringResponse) -> dict:
    out: dict = {}
    if "transit_gateway_peering" in value:
        import aws_sdk_networkmanager.types.transit_gateway_peering

        out["TransitGatewayPeering"] = (
            aws_sdk_networkmanager.types.transit_gateway_peering.serialize_json(
                value["transit_gateway_peering"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTransitGatewayPeeringResponse:
    out: GetTransitGatewayPeeringResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayPeering" in data:
        import aws_sdk_networkmanager.types.transit_gateway_peering

        out["transit_gateway_peering"] = (
            aws_sdk_networkmanager.types.transit_gateway_peering.deserialize_json(
                data["TransitGatewayPeering"]
            )
        )
    return out
