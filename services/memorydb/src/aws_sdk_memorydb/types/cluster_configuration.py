"""Generated from Smithy shape ``com.amazonaws.memorydb#ClusterConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.shard_details
    import aws_sdk_memorydb.types.string


class ClusterConfiguration(TypedDict):
    name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the cluster</p>"""
    description: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The description of the cluster configuration</p>"""
    node_type: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The node type used for the cluster</p>"""
    engine: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the engine used by the cluster configuration.</p>"""
    engine_version: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The Redis OSS engine version used by the cluster</p>"""
    maintenance_window: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The specified maintenance window for the cluster</p>"""
    topic_arn: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the SNS notification topic for the cluster</p>"""
    port: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The port used by the cluster</p>"""
    parameter_group_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of parameter group used by the cluster</p>"""
    subnet_group_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the subnet group used by the cluster</p>"""
    vpc_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The ID of the VPC the cluster belongs to</p>"""
    snapshot_retention_limit: NotRequired[
        "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The snapshot retention limit set by the cluster</p>"""
    snapshot_window: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The snapshot window set by the cluster</p>"""
    num_shards: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of shards in the cluster</p>"""
    shards: NotRequired["aws_sdk_memorydb.types.shard_details.ShardDetails"]
    """<p>The list of shards in the cluster</p>"""
    multi_region_parameter_group_name: NotRequired[
        "aws_sdk_memorydb.types.string.String"
    ]
    """<p>The name of the multi-Region parameter group associated with the cluster configuration.</p>"""
    multi_region_cluster_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name for the multi-Region cluster associated with the cluster configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterConfiguration) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "maintenance_window" in value:
        out["MaintenanceWindow"] = value["maintenance_window"]
    if "topic_arn" in value:
        out["TopicArn"] = value["topic_arn"]
    if "port" in value:
        out["Port"] = value["port"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "subnet_group_name" in value:
        out["SubnetGroupName"] = value["subnet_group_name"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "snapshot_retention_limit" in value:
        out["SnapshotRetentionLimit"] = value["snapshot_retention_limit"]
    if "snapshot_window" in value:
        out["SnapshotWindow"] = value["snapshot_window"]
    if "num_shards" in value:
        out["NumShards"] = value["num_shards"]
    if "shards" in value:
        import aws_sdk_memorydb.types.shard_details

        out["Shards"] = aws_sdk_memorydb.types.shard_details.serialize_aws_json_1_1(
            value["shards"]
        )
    if "multi_region_parameter_group_name" in value:
        out["MultiRegionParameterGroupName"] = value[
            "multi_region_parameter_group_name"
        ]
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterConfiguration:
    out: ClusterConfiguration = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "MaintenanceWindow" in data:
        out["maintenance_window"] = data["MaintenanceWindow"]
    if "TopicArn" in data:
        out["topic_arn"] = data["TopicArn"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if "SubnetGroupName" in data:
        out["subnet_group_name"] = data["SubnetGroupName"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SnapshotRetentionLimit" in data:
        out["snapshot_retention_limit"] = data["SnapshotRetentionLimit"]
    if "SnapshotWindow" in data:
        out["snapshot_window"] = data["SnapshotWindow"]
    if "NumShards" in data:
        out["num_shards"] = data["NumShards"]
    if "Shards" in data:
        import aws_sdk_memorydb.types.shard_details

        out["shards"] = aws_sdk_memorydb.types.shard_details.deserialize_aws_json_1_1(
            data["Shards"]
        )
    if "MultiRegionParameterGroupName" in data:
        out["multi_region_parameter_group_name"] = data["MultiRegionParameterGroupName"]
    if "MultiRegionClusterName" in data:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    return out
