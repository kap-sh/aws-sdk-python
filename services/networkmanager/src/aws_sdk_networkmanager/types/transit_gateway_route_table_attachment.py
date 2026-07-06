"""Generated from Smithy shape ``com.amazonaws.networkmanager#TransitGatewayRouteTableAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment
    import aws_sdk_networkmanager.types.peering_id
    import aws_sdk_networkmanager.types.transit_gateway_route_table_arn


class TransitGatewayRouteTableAttachment(TypedDict, closed=True):
    attachment: NotRequired["aws_sdk_networkmanager.types.attachment.Attachment"]
    peering_id: NotRequired["aws_sdk_networkmanager.types.peering_id.PeeringId"]
    """<p>The ID of the peering attachment.</p>"""
    transit_gateway_route_table_arn: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_route_table_arn.TransitGatewayRouteTableArn"
    ]
    r"""<p>The ARN of the transit gateway attachment route table. For example, <code>\"TransitGatewayRouteTableArn\": \"arn:aws:ec2:us-west-2:123456789012:transit-gateway-route-table/tgw-rtb-9876543210123456\"</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransitGatewayRouteTableAttachment) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_networkmanager.types.attachment

        out["Attachment"] = aws_sdk_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    if "peering_id" in value:
        out["PeeringId"] = value["peering_id"]
    if "transit_gateway_route_table_arn" in value:
        out["TransitGatewayRouteTableArn"] = value["transit_gateway_route_table_arn"]
    return out


def deserialize_json(data: dict) -> TransitGatewayRouteTableAttachment:
    out: TransitGatewayRouteTableAttachment = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import aws_sdk_networkmanager.types.attachment

        out["attachment"] = aws_sdk_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    if "PeeringId" in data:
        out["peering_id"] = data["PeeringId"]
    if "TransitGatewayRouteTableArn" in data:
        out["transit_gateway_route_table_arn"] = data["TransitGatewayRouteTableArn"]
    return out
