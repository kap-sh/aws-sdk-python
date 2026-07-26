"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateTransitGatewayRouteTableAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.transit_gateway_route_table_attachment


class CreateTransitGatewayRouteTableAttachmentResponse(TypedDict, closed=True):
    transit_gateway_route_table_attachment: NotRequired[
        "capo_networkmanager.types.transit_gateway_route_table_attachment.TransitGatewayRouteTableAttachment"
    ]
    """<p>The route table associated with the create transit gateway route table attachment request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTransitGatewayRouteTableAttachmentResponse) -> dict:
    out: dict = {}
    if "transit_gateway_route_table_attachment" in value:
        import capo_networkmanager.types.transit_gateway_route_table_attachment

        out["TransitGatewayRouteTableAttachment"] = (
            capo_networkmanager.types.transit_gateway_route_table_attachment.serialize_json(
                value["transit_gateway_route_table_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateTransitGatewayRouteTableAttachmentResponse:
    out: CreateTransitGatewayRouteTableAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayRouteTableAttachment" in data:
        import capo_networkmanager.types.transit_gateway_route_table_attachment

        out["transit_gateway_route_table_attachment"] = (
            capo_networkmanager.types.transit_gateway_route_table_attachment.deserialize_json(
                data["TransitGatewayRouteTableAttachment"]
            )
        )
    return out
