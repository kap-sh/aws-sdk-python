"""Generated from Smithy shape ``com.amazonaws.networkmanager#RoutingInformationNextHop``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.ip_address


class RoutingInformationNextHop(TypedDict, closed=True):
    ip_address: NotRequired["aws_sdk_networkmanager.types.ip_address.IPAddress"]
    """<p>The IP address of the next hop.</p>"""
    core_network_attachment_id: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the core network attachment for the next hop.</p>"""
    resource_id: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The ID of the resource for the next hop.</p>"""
    resource_type: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The type of resource for the next hop.</p>"""
    segment_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of the segment for the next hop.</p>"""
    edge_location: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The edge location for the next hop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingInformationNextHop) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    if "core_network_attachment_id" in value:
        out["CoreNetworkAttachmentId"] = value["core_network_attachment_id"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    return out


def deserialize_json(data: dict) -> RoutingInformationNextHop:
    out: RoutingInformationNextHop = {}  # type: ignore[typeddict-item]
    if "IpAddress" in data:
        out["ip_address"] = data["IpAddress"]
    if "CoreNetworkAttachmentId" in data:
        out["core_network_attachment_id"] = data["CoreNetworkAttachmentId"]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    return out
