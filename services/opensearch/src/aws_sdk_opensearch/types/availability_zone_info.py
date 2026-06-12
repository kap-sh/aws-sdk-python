"""Generated from Smithy shape ``com.amazonaws.opensearch#AvailabilityZoneInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.availability_zone
    import aws_sdk_opensearch.types.number_of_nodes
    import aws_sdk_opensearch.types.number_of_shards
    import aws_sdk_opensearch.types.zone_status


class AvailabilityZoneInfo(TypedDict):
    availability_zone_name: NotRequired[
        "aws_sdk_opensearch.types.availability_zone.AvailabilityZone"
    ]
    """<p>The name of the Availability Zone.</p>"""
    zone_status: NotRequired["aws_sdk_opensearch.types.zone_status.ZoneStatus"]
    """<p>The current state of the Availability Zone. Current options are <code>Active</code> and <code>StandBy</code>.</p> <ul> <li> <p> <code>Active</code> - Data nodes in the Availability Zone are in use.</p> </li> <li> <p> <code>StandBy</code> - Data nodes in the Availability Zone are in a standby state.</p> </li> <li> <p> <code>NotAvailable</code> - Unable to retrieve information.</p> </li> </ul>"""
    configured_data_node_count: NotRequired[
        "aws_sdk_opensearch.types.number_of_nodes.NumberOfNodes"
    ]
    """<p>The total number of data nodes configured in the Availability Zone.</p>"""
    available_data_node_count: NotRequired[
        "aws_sdk_opensearch.types.number_of_nodes.NumberOfNodes"
    ]
    """<p>The number of data nodes active in the Availability Zone.</p>"""
    total_shards: NotRequired[
        "aws_sdk_opensearch.types.number_of_shards.NumberOfShards"
    ]
    """<p>The total number of primary and replica shards in the Availability Zone.</p>"""
    total_un_assigned_shards: NotRequired[
        "aws_sdk_opensearch.types.number_of_shards.NumberOfShards"
    ]
    """<p>The total number of primary and replica shards that aren't allocated to any of the nodes in the Availability Zone.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailabilityZoneInfo) -> dict:
    out: dict = {}
    if "availability_zone_name" in value:
        out["AvailabilityZoneName"] = value["availability_zone_name"]
    if "zone_status" in value:
        import aws_sdk_opensearch.types.zone_status

        out["ZoneStatus"] = aws_sdk_opensearch.types.zone_status.serialize_json(
            value["zone_status"]
        )
    if "configured_data_node_count" in value:
        out["ConfiguredDataNodeCount"] = value["configured_data_node_count"]
    if "available_data_node_count" in value:
        out["AvailableDataNodeCount"] = value["available_data_node_count"]
    if "total_shards" in value:
        out["TotalShards"] = value["total_shards"]
    if "total_un_assigned_shards" in value:
        out["TotalUnAssignedShards"] = value["total_un_assigned_shards"]
    return out


def deserialize_json(data: dict) -> AvailabilityZoneInfo:
    out: AvailabilityZoneInfo = {}  # type: ignore[typeddict-item]
    if "AvailabilityZoneName" in data:
        out["availability_zone_name"] = data["AvailabilityZoneName"]
    if "ZoneStatus" in data:
        import aws_sdk_opensearch.types.zone_status

        out["zone_status"] = aws_sdk_opensearch.types.zone_status.deserialize_json(
            data["ZoneStatus"]
        )
    if "ConfiguredDataNodeCount" in data:
        out["configured_data_node_count"] = data["ConfiguredDataNodeCount"]
    if "AvailableDataNodeCount" in data:
        out["available_data_node_count"] = data["AvailableDataNodeCount"]
    if "TotalShards" in data:
        out["total_shards"] = data["TotalShards"]
    if "TotalUnAssignedShards" in data:
        out["total_un_assigned_shards"] = data["TotalUnAssignedShards"]
    return out
