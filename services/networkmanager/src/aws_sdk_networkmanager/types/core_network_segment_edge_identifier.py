"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkSegmentEdgeIdentifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.external_region_code


class CoreNetworkSegmentEdgeIdentifier(TypedDict):
    core_network_id: NotRequired[
        "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    segment_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of the segment edge.</p>"""
    edge_location: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Region where the segment edge is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkSegmentEdgeIdentifier) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    return out


def deserialize_json(data: dict) -> CoreNetworkSegmentEdgeIdentifier:
    out: CoreNetworkSegmentEdgeIdentifier = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    return out
