"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisEndpointOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.ip_address
    import aws_sdk_networkmanager.types.transit_gateway_arn
    import aws_sdk_networkmanager.types.transit_gateway_attachment_arn


class RouteAnalysisEndpointOptions(TypedDict):
    transit_gateway_attachment_arn: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_attachment_arn.TransitGatewayAttachmentArn"
    ]
    """<p>The ARN of the transit gateway attachment.</p>"""
    transit_gateway_arn: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_arn.TransitGatewayArn"
    ]
    """<p>The ARN of the transit gateway.</p>"""
    ip_address: NotRequired["aws_sdk_networkmanager.types.ip_address.IPAddress"]
    """<p>The IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAnalysisEndpointOptions) -> dict:
    out: dict = {}
    if "transit_gateway_attachment_arn" in value:
        out["TransitGatewayAttachmentArn"] = value["transit_gateway_attachment_arn"]
    if "transit_gateway_arn" in value:
        out["TransitGatewayArn"] = value["transit_gateway_arn"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    return out


def deserialize_json(data: dict) -> RouteAnalysisEndpointOptions:
    out: RouteAnalysisEndpointOptions = {}  # type: ignore[typeddict-item]
    if "TransitGatewayAttachmentArn" in data:
        out["transit_gateway_attachment_arn"] = data["TransitGatewayAttachmentArn"]
    if "TransitGatewayArn" in data:
        out["transit_gateway_arn"] = data["TransitGatewayArn"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    return out
