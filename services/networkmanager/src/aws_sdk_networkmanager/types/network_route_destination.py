"""Generated from Smithy shape ``com.amazonaws.networkmanager#NetworkRouteDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.transit_gateway_attachment_id


class NetworkRouteDestination(TypedDict, closed=True):
    core_network_attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    ]
    """<p>The ID of a core network attachment.</p>"""
    transit_gateway_attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.transit_gateway_attachment_id.TransitGatewayAttachmentId"
    ]
    """<p>The ID of the transit gateway attachment.</p>"""
    segment_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of the segment.</p>"""
    network_function_group_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The network function group name associated with the destination.</p>"""
    edge_location: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The edge location for the network destination.</p>"""
    resource_type: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The resource type.</p>"""
    resource_id: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkRouteDestination) -> dict:
    out: dict = {}
    if "core_network_attachment_id" in value:
        out["CoreNetworkAttachmentId"] = value["core_network_attachment_id"]
    if "transit_gateway_attachment_id" in value:
        out["TransitGatewayAttachmentId"] = value["transit_gateway_attachment_id"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "network_function_group_name" in value:
        out["NetworkFunctionGroupName"] = value["network_function_group_name"]
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    return out


def deserialize_json(data: dict) -> NetworkRouteDestination:
    out: NetworkRouteDestination = {}  # type: ignore[typeddict-item]
    if "CoreNetworkAttachmentId" in data:
        out["core_network_attachment_id"] = data["CoreNetworkAttachmentId"]
    if "TransitGatewayAttachmentId" in data:
        out["transit_gateway_attachment_id"] = data["TransitGatewayAttachmentId"]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    if "NetworkFunctionGroupName" in data:
        out["network_function_group_name"] = data["NetworkFunctionGroupName"]
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    return out
