"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetTransitGatewayRouteTableAttachmentResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.transit_gateway_route_table_attachment


class GetTransitGatewayRouteTableAttachmentResponse(TypedDict):
    transit_gateway_route_table_attachment: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_route_table_attachment.TransitGatewayRouteTableAttachment"
    ]
    """<p>Returns information about the transit gateway route table attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransitGatewayRouteTableAttachmentResponse) -> dict:
    out: dict = {}
    if "transit_gateway_route_table_attachment" in value:
        import aws_sdk_networkmanager.types.transit_gateway_route_table_attachment

        out["TransitGatewayRouteTableAttachment"] = (
            aws_sdk_networkmanager.types.transit_gateway_route_table_attachment.serialize_json(
                value["transit_gateway_route_table_attachment"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTransitGatewayRouteTableAttachmentResponse:
    out: GetTransitGatewayRouteTableAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "TransitGatewayRouteTableAttachment" in data:
        import aws_sdk_networkmanager.types.transit_gateway_route_table_attachment

        out["transit_gateway_route_table_attachment"] = (
            aws_sdk_networkmanager.types.transit_gateway_route_table_attachment.deserialize_json(
                data["TransitGatewayRouteTableAttachment"]
            )
        )
    return out
