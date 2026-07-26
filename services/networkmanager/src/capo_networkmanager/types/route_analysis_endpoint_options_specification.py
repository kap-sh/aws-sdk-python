"""Generated from Smithy shape ``com.amazonaws.networkmanager#RouteAnalysisEndpointOptionsSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.ip_address
    import capo_networkmanager.types.transit_gateway_attachment_arn


class RouteAnalysisEndpointOptionsSpecification(TypedDict, closed=True):
    transit_gateway_attachment_arn: NotRequired[
        "capo_networkmanager.types.transit_gateway_attachment_arn.TransitGatewayAttachmentArn"
    ]
    """<p>The ARN of the transit gateway attachment.</p>"""
    ip_address: NotRequired["capo_networkmanager.types.ip_address.IPAddress"]
    """<p>The IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteAnalysisEndpointOptionsSpecification) -> dict:
    out: dict = {}
    if "transit_gateway_attachment_arn" in value:
        out["TransitGatewayAttachmentArn"] = value["transit_gateway_attachment_arn"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    return out


def deserialize_json(data: dict) -> RouteAnalysisEndpointOptionsSpecification:
    out: RouteAnalysisEndpointOptionsSpecification = {}  # type: ignore[typeddict-item]
    if "TransitGatewayAttachmentArn" in data:
        out["transit_gateway_attachment_arn"] = data["TransitGatewayAttachmentArn"]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    return out
