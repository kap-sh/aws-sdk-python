"""Generated from Smithy shape ``com.amazonaws.connect#GlobalResiliencyMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.active_region
    import aws_sdk_connect.types.origin_region
    import aws_sdk_connect.types.traffic_distribution_group_id


class GlobalResiliencyMetadata(TypedDict):
    active_region: NotRequired["aws_sdk_connect.types.active_region.ActiveRegion"]
    """<p>The current AWS region in which the contact is active. This indicates where the contact is being processed in real-time.</p>"""
    origin_region: NotRequired["aws_sdk_connect.types.origin_region.OriginRegion"]
    """<p>The AWS region where the contact was originally created and initiated. This may differ from the ActiveRegion if the contact has been transferred across regions.</p>"""
    traffic_distribution_group_id: NotRequired[
        "aws_sdk_connect.types.traffic_distribution_group_id.TrafficDistributionGroupId"
    ]
    """<p>The identifier of the traffic distribution group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GlobalResiliencyMetadata) -> dict:
    out: dict = {}
    if "active_region" in value:
        out["ActiveRegion"] = value["active_region"]
    if "origin_region" in value:
        out["OriginRegion"] = value["origin_region"]
    if "traffic_distribution_group_id" in value:
        out["TrafficDistributionGroupId"] = value["traffic_distribution_group_id"]
    return out


def deserialize_json(data: dict) -> GlobalResiliencyMetadata:
    out: GlobalResiliencyMetadata = {}  # type: ignore[typeddict-item]
    if "ActiveRegion" in data:
        out["active_region"] = data["ActiveRegion"]
    if "OriginRegion" in data:
        out["origin_region"] = data["OriginRegion"]
    if "TrafficDistributionGroupId" in data:
        out["traffic_distribution_group_id"] = data["TrafficDistributionGroupId"]
    return out
