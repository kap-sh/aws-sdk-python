"""Generated from Smithy shape ``com.amazonaws.memorydb#Node``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.endpoint
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.t_stamp


class Node(TypedDict):
    name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The node identifier. A node name is a numeric identifier (0001, 0002, etc.). The combination of cluster name, shard name and node name uniquely identifies every node used in a customer's Amazon account.</p>"""
    status: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The status of the service update on the node</p>"""
    availability_zone: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The Availability Zone in which the node resides</p>"""
    create_time: NotRequired["aws_sdk_memorydb.types.t_stamp.TStamp"]
    """<p>The date and time when the node was created.</p>"""
    endpoint: NotRequired["aws_sdk_memorydb.types.endpoint.Endpoint"]
    """<p>The hostname for connecting to this node.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Node) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        out["Status"] = value["status"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "create_time" in value:
        import aws_sdk_memorydb.types.t_stamp

        out["CreateTime"] = aws_sdk_memorydb.types.t_stamp.serialize_aws_json_1_1(
            value["create_time"]
        )
    if "endpoint" in value:
        import aws_sdk_memorydb.types.endpoint

        out["Endpoint"] = aws_sdk_memorydb.types.endpoint.serialize_aws_json_1_1(
            value["endpoint"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Node:
    out: Node = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "CreateTime" in data:
        import aws_sdk_memorydb.types.t_stamp

        out["create_time"] = aws_sdk_memorydb.types.t_stamp.deserialize_aws_json_1_1(
            data["CreateTime"]
        )
    if "Endpoint" in data:
        import aws_sdk_memorydb.types.endpoint

        out["endpoint"] = aws_sdk_memorydb.types.endpoint.deserialize_aws_json_1_1(
            data["Endpoint"]
        )
    return out
