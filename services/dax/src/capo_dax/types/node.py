"""Generated from Smithy shape ``com.amazonaws.dax#Node``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.endpoint
    import capo_dax.types.string
    import capo_dax.types.t_stamp


class Node(TypedDict, closed=True):
    node_id: NotRequired["capo_dax.types.string.String"]
    """<p>A system-generated identifier for the node.</p>"""
    endpoint: NotRequired["capo_dax.types.endpoint.Endpoint"]
    """<p>The endpoint for the node, consisting of a DNS name and a port number. Client applications can connect directly to a node endpoint, if desired (as an alternative to allowing DAX client software to intelligently route requests and responses to nodes in the DAX cluster.</p>"""
    node_create_time: NotRequired["capo_dax.types.t_stamp.TStamp"]
    """<p>The date and time (in UNIX epoch format) when the node was launched.</p>"""
    availability_zone: NotRequired["capo_dax.types.string.String"]
    """<p>The Availability Zone (AZ) in which the node has been deployed.</p>"""
    node_status: NotRequired["capo_dax.types.string.String"]
    """<p>The current status of the node. For example: <code>available</code>.</p>"""
    parameter_group_status: NotRequired["capo_dax.types.string.String"]
    """<p>The status of the parameter group associated with this node. For example, <code>in-sync</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Node) -> dict:
    out: dict = {}
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "endpoint" in value:
        import capo_dax.types.endpoint

        out["Endpoint"] = capo_dax.types.endpoint.serialize_aws_json_1_1(
            value["endpoint"]
        )
    if "node_create_time" in value:
        import capo_dax.types.t_stamp

        out["NodeCreateTime"] = capo_dax.types.t_stamp.serialize_aws_json_1_1(
            value["node_create_time"]
        )
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "node_status" in value:
        out["NodeStatus"] = value["node_status"]
    if "parameter_group_status" in value:
        out["ParameterGroupStatus"] = value["parameter_group_status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "Endpoint" in data:
        import capo_dax.types.endpoint

        out["endpoint"] = capo_dax.types.endpoint.deserialize_aws_json_1_1(
            data["Endpoint"]
        )
    if "NodeCreateTime" in data:
        import capo_dax.types.t_stamp

        out["node_create_time"] = capo_dax.types.t_stamp.deserialize_aws_json_1_1(
            data["NodeCreateTime"]
        )
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "NodeStatus" in data:
        out["node_status"] = data["NodeStatus"]
    if "ParameterGroupStatus" in data:
        out["parameter_group_status"] = data["ParameterGroupStatus"]
    return out
