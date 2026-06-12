"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainNodesStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.availability_zone
    import aws_sdk_opensearch.types.node_id
    import aws_sdk_opensearch.types.node_status
    import aws_sdk_opensearch.types.node_type
    import aws_sdk_opensearch.types.open_search_partition_instance_type
    import aws_sdk_opensearch.types.storage_type_name
    import aws_sdk_opensearch.types.volume_size
    import aws_sdk_opensearch.types.volume_type


class DomainNodesStatus(TypedDict):
    node_id: NotRequired["aws_sdk_opensearch.types.node_id.NodeId"]
    """<p>The ID of the node.</p>"""
    node_type: NotRequired["aws_sdk_opensearch.types.node_type.NodeType"]
    """<p>Indicates whether the nodes is a data, master, or UltraWarm node.</p>"""
    availability_zone: NotRequired[
        "aws_sdk_opensearch.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone of the node.</p>"""
    instance_type: NotRequired[
        "aws_sdk_opensearch.types.open_search_partition_instance_type.OpenSearchPartitionInstanceType"
    ]
    """<p>The instance type information of the node.</p>"""
    node_status: NotRequired["aws_sdk_opensearch.types.node_status.NodeStatus"]
    """<p>Indicates if the node is active or in standby.</p>"""
    storage_type: NotRequired[
        "aws_sdk_opensearch.types.storage_type_name.StorageTypeName"
    ]
    """<p>Indicates if the node has EBS or instance storage. </p>"""
    storage_volume_type: NotRequired["aws_sdk_opensearch.types.volume_type.VolumeType"]
    """<p>If the nodes has EBS storage, indicates if the volume type is gp2 or gp3. Only applicable for data nodes. </p>"""
    storage_size: NotRequired["aws_sdk_opensearch.types.volume_size.VolumeSize"]
    """<p>The storage size of the node, in GiB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DomainNodesStatus) -> dict:
    out: dict = {}
    if "node_id" in value:
        out["NodeId"] = value["node_id"]
    if "node_type" in value:
        import aws_sdk_opensearch.types.node_type

        out["NodeType"] = aws_sdk_opensearch.types.node_type.serialize_json(
            value["node_type"]
        )
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "instance_type" in value:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["InstanceType"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.serialize_json(
                value["instance_type"]
            )
        )
    if "node_status" in value:
        import aws_sdk_opensearch.types.node_status

        out["NodeStatus"] = aws_sdk_opensearch.types.node_status.serialize_json(
            value["node_status"]
        )
    if "storage_type" in value:
        out["StorageType"] = value["storage_type"]
    if "storage_volume_type" in value:
        import aws_sdk_opensearch.types.volume_type

        out["StorageVolumeType"] = aws_sdk_opensearch.types.volume_type.serialize_json(
            value["storage_volume_type"]
        )
    if "storage_size" in value:
        out["StorageSize"] = value["storage_size"]
    return out


def deserialize_json(data: dict) -> DomainNodesStatus:
    out: DomainNodesStatus = {}  # type: ignore[typeddict-item]
    if "NodeId" in data:
        out["node_id"] = data["NodeId"]
    if "NodeType" in data:
        import aws_sdk_opensearch.types.node_type

        out["node_type"] = aws_sdk_opensearch.types.node_type.deserialize_json(
            data["NodeType"]
        )
    if "AvailabilityZone" in data:
        out["availability_zone"] = data["AvailabilityZone"]
    if "InstanceType" in data:
        import aws_sdk_opensearch.types.open_search_partition_instance_type

        out["instance_type"] = (
            aws_sdk_opensearch.types.open_search_partition_instance_type.deserialize_json(
                data["InstanceType"]
            )
        )
    if "NodeStatus" in data:
        import aws_sdk_opensearch.types.node_status

        out["node_status"] = aws_sdk_opensearch.types.node_status.deserialize_json(
            data["NodeStatus"]
        )
    if "StorageType" in data:
        out["storage_type"] = data["StorageType"]
    if "StorageVolumeType" in data:
        import aws_sdk_opensearch.types.volume_type

        out["storage_volume_type"] = (
            aws_sdk_opensearch.types.volume_type.deserialize_json(
                data["StorageVolumeType"]
            )
        )
    if "StorageSize" in data:
        out["storage_size"] = data["StorageSize"]
    return out
