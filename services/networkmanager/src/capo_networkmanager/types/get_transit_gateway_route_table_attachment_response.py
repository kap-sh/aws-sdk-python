"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayRouteTableAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.transit_gateway_route_table_attachment


class GetTransitGatewayRouteTableAttachmentResponse(TypedDict, closed=True):
    transit_gateway_route_table_attachment: NotRequired[
        "capo_networkmanager.types.transit_gateway_route_table_attachment.TransitGatewayRouteTableAttachment"
    ]
    """<p>Returns information about the transit gateway route table attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayRouteTableAttachmentResponse) -> dict:
    out: dict = {}
    if "transit_gateway_route_table_attachment" in value:
        import capo_networkmanager.types.transit_gateway_route_table_attachment

        out["TransitGatewayRouteTableAttachment"] = (
            capo_networkmanager.types.transit_gateway_route_table_attachment.serialize_json(
                value["transit_gateway_route_table_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTransitGatewayRouteTableAttachmentResponse:
    out: GetTransitGatewayRouteTableAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayRouteTableAttachment" in data:
        import capo_networkmanager.types.transit_gateway_route_table_attachment

        out["transit_gateway_route_table_attachment"] = (
            capo_networkmanager.types.transit_gateway_route_table_attachment.deserialize_json(
                data["TransitGatewayRouteTableAttachment"]
            )
        )
    return out
