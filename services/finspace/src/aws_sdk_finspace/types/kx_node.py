"""Generated from Smithy shape ``com.amazonaws.finspace#KxNode``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.availability_zone_id
    import aws_sdk_finspace.types.kx_cluster_node_id_string
    import aws_sdk_finspace.types.kx_node_status
    import aws_sdk_finspace.types.timestamp


class KxNode(TypedDict, closed=True):
    node_id: NotRequired[
        "aws_sdk_finspace.types.kx_cluster_node_id_string.KxClusterNodeIdString"
    ]
    """<p>A unique identifier for the node.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_finspace.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The identifier of the availability zones where subnets for the environment are created.</p>"""
    launch_time: NotRequired["aws_sdk_finspace.types.timestamp.Timestamp"]
    """<p>The time when a particular node is started. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.</p>"""
    status: NotRequired["aws_sdk_finspace.types.kx_node_status.KxNodeStatus"]
    """<p> Specifies the status of the cluster nodes. </p> <ul> <li> <p> <code>RUNNING</code> – The node is actively serving.</p> </li> <li> <p> <code>PROVISIONING</code> – The node is being prepared.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: KxNode) -> dict:
    out: dict = {}
    if "node_id" in value:
        out["nodeId"] = value["node_id"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "launch_time" in value:
        import aws_sdk_finspace.types.timestamp

        out["launchTime"] = aws_sdk_finspace.types.timestamp.serialize_json(
            value["launch_time"]
        )
    if "status" in value:
        import aws_sdk_finspace.types.kx_node_status

        out["status"] = aws_sdk_finspace.types.kx_node_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> KxNode:
    out: KxNode = {}  # type: ignore[typeddict-item]
    if "nodeId" in data:
        out["node_id"] = data["nodeId"]
    if "availabilityZoneId" in data:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if "launchTime" in data:
        import aws_sdk_finspace.types.timestamp

        out["launch_time"] = aws_sdk_finspace.types.timestamp.deserialize_json(
            data["launchTime"]
        )
    if "status" in data:
        import aws_sdk_finspace.types.kx_node_status

        out["status"] = aws_sdk_finspace.types.kx_node_status.deserialize_json(
            data["status"]
        )
    return out
