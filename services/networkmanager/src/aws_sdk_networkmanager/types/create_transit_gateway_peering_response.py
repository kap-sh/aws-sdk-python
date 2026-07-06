"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateTransitGatewayPeeringResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.transit_gateway_peering


class CreateTransitGatewayPeeringResponse(TypedDict, closed=True):
    transit_gateway_peering: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_peering.TransitGatewayPeering"
    ]
    """<p>Returns information about the transit gateway peering connection request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTransitGatewayPeeringResponse) -> dict:
    out: dict = {}
    if "transit_gateway_peering" in value:
        import aws_sdk_networkmanager.types.transit_gateway_peering

        out["TransitGatewayPeering"] = (
            aws_sdk_networkmanager.types.transit_gateway_peering.serialize_json(
                value["transit_gateway_peering"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTransitGatewayPeeringResponse:
    out: CreateTransitGatewayPeeringResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayPeering" in data:
        import aws_sdk_networkmanager.types.transit_gateway_peering

        out["transit_gateway_peering"] = (
            aws_sdk_networkmanager.types.transit_gateway_peering.deserialize_json(
                data["TransitGatewayPeering"]
            )
        )
    return out
