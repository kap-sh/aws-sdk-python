"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.acl_name
    import aws_sdk_memorydb.types.boolean_optional
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.ip_discovery
    import aws_sdk_memorydb.types.network_type
    import aws_sdk_memorydb.types.security_group_ids_list
    import aws_sdk_memorydb.types.snapshot_arns_list
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.tag_list


class CreateClusterRequest(TypedDict):
    cluster_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the cluster. This value must be unique as it also serves as the cluster identifier.</p>"""
    node_type: "aws_sdk_memorydb.types.string.String"
    """<p>The compute and memory capacity of the nodes in the cluster.</p>"""
    multi_region_cluster_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the multi-Region cluster to be created.</p>"""
    parameter_group_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the parameter group associated with the cluster.</p>"""
    description: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>An optional description of the cluster.</p>"""
    num_shards: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The number of shards the cluster will contain. The default value is 1. </p>"""
    num_replicas_per_shard: NotRequired[
        "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of replicas to apply to each shard. The default value is 1. The maximum is 5. </p>"""
    subnet_group_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the subnet group to be used for the cluster.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_memorydb.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>A list of security group names to associate with this cluster.</p>"""
    maintenance_window: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>"""
    port: NotRequired["aws_sdk_memorydb.types.integer_optional.IntegerOptional"]
    """<p>The port number on which each of the nodes accepts connections.</p>"""
    sns_topic_arn: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Simple Notification Service (SNS) topic to which notifications are sent.</p>"""
    tls_enabled: NotRequired["aws_sdk_memorydb.types.boolean_optional.BooleanOptional"]
    """<p>A flag to enable in-transit encryption on the cluster.</p>"""
    kms_key_id: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The ID of the KMS key used to encrypt the cluster.</p>"""
    snapshot_arns: NotRequired[
        "aws_sdk_memorydb.types.snapshot_arns_list.SnapshotArnsList"
    ]
    """<p>A list of Amazon Resource Names (ARN) that uniquely identify the RDB snapshot files stored in Amazon S3. The snapshot files are used to populate the new cluster. The Amazon S3 object name in the ARN cannot contain any commas.</p>"""
    snapshot_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of a snapshot from which to restore data into the new cluster. The snapshot status changes to restoring while the new cluster is being created.</p>"""
    snapshot_retention_limit: NotRequired[
        "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which MemoryDB retains automatic snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p>"""
    tags: NotRequired["aws_sdk_memorydb.types.tag_list.TagList"]
    """<p>A list of tags to be added to this resource. Tags are comma-separated key,value pairs (e.g. Key=myKey, Value=myKeyValue. You can include multiple tags as shown following: Key=myKey, Value=myKeyValue Key=mySecondKey, Value=mySecondKeyValue.</p>"""
    snapshot_window: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your shard.</p> <p> Example: 05:00-09:00</p> <p> If you do not specify this parameter, MemoryDB automatically chooses an appropriate time range.</p>"""
    acl_name: "aws_sdk_memorydb.types.acl_name.ACLName"
    """<p>The name of the Access Control List to associate with the cluster.</p>"""
    engine: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the engine to be used for the cluster.</p>"""
    engine_version: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The version number of the Redis OSS engine to be used for the cluster.</p>"""
    auto_minor_version_upgrade: NotRequired[
        "aws_sdk_memorydb.types.boolean_optional.BooleanOptional"
    ]
    """<p>When set to true, the cluster will automatically receive minor engine version upgrades after launch.</p>"""
    data_tiering: NotRequired["aws_sdk_memorydb.types.boolean_optional.BooleanOptional"]
    """<p>Enables data tiering. Data tiering is only supported for clusters using the r6gd node type. This parameter must be set when using r6gd nodes. For more information, see <a href=\"https://docs.aws.amazon.com/memorydb/latest/devguide/data-tiering.html\">Data tiering</a>.</p>"""
    network_type: NotRequired["aws_sdk_memorydb.types.network_type.NetworkType"]
    """<p>Specifies the IP address type for the cluster. Valid values are 'ipv4', 'ipv6', or 'dual_stack'. When set to 'ipv4', the cluster will only be accessible via IPv4 addresses. When set to 'ipv6', the cluster will only be accessible via IPv6 addresses. When set to 'dual_stack', the cluster will be accessible via both IPv4 and IPv6 addresses. If not specified, the default is 'ipv4'.</p>"""
    ip_discovery: NotRequired["aws_sdk_memorydb.types.ip_discovery.IpDiscovery"]
    """<p>The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are 'ipv4' or 'ipv6'. When set to 'ipv4', cluster discovery functions such as cluster slots, cluster shards, and cluster nodes return IPv4 addresses for cluster nodes. When set to 'ipv6', the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is 'ipv4'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    out["NodeType"] = value["node_type"]
    if "multi_region_cluster_name" in value:
        out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "num_shards" in value:
        out["NumShards"] = value["num_shards"]
    if "num_replicas_per_shard" in value:
        out["NumReplicasPerShard"] = value["num_replicas_per_shard"]
    if "subnet_group_name" in value:
        out["SubnetGroupName"] = value["subnet_group_name"]
    if "security_group_ids" in value:
        import aws_sdk_memorydb.types.security_group_ids_list

        out["SecurityGroupIds"] = (
            aws_sdk_memorydb.types.security_group_ids_list.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "maintenance_window" in value:
        out["MaintenanceWindow"] = value["maintenance_window"]
    if "port" in value:
        out["Port"] = value["port"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "tls_enabled" in value:
        out["TLSEnabled"] = value["tls_enabled"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "snapshot_arns" in value:
        import aws_sdk_memorydb.types.snapshot_arns_list

        out["SnapshotArns"] = (
            aws_sdk_memorydb.types.snapshot_arns_list.serialize_aws_json_1_1(
                value["snapshot_arns"]
            )
        )
    if "snapshot_name" in value:
        out["SnapshotName"] = value["snapshot_name"]
    if "snapshot_retention_limit" in value:
        out["SnapshotRetentionLimit"] = value["snapshot_retention_limit"]
    if "tags" in value:
        import aws_sdk_memorydb.types.tag_list

        out["Tags"] = aws_sdk_memorydb.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "snapshot_window" in value:
        out["SnapshotWindow"] = value["snapshot_window"]
    out["ACLName"] = value["acl_name"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "auto_minor_version_upgrade" in value:
        out["AutoMinorVersionUpgrade"] = value["auto_minor_version_upgrade"]
    if "data_tiering" in value:
        out["DataTiering"] = value["data_tiering"]
    if "network_type" in value:
        import aws_sdk_memorydb.types.network_type

        out["NetworkType"] = aws_sdk_memorydb.types.network_type.serialize_aws_json_1_1(
            value["network_type"]
        )
    if "ip_discovery" in value:
        import aws_sdk_memorydb.types.ip_discovery

        out["IpDiscovery"] = aws_sdk_memorydb.types.ip_discovery.serialize_aws_json_1_1(
            value["ip_discovery"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError("CreateClusterRequest.cluster_name required")
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    else:
        raise DeserializationError("CreateClusterRequest.node_type required")
    if "MultiRegionClusterName" in data:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "NumShards" in data:
        out["num_shards"] = data["NumShards"]
    if "NumReplicasPerShard" in data:
        out["num_replicas_per_shard"] = data["NumReplicasPerShard"]
    if "SubnetGroupName" in data:
        out["subnet_group_name"] = data["SubnetGroupName"]
    if "SecurityGroupIds" in data:
        import aws_sdk_memorydb.types.security_group_ids_list

        out["security_group_ids"] = (
            aws_sdk_memorydb.types.security_group_ids_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "MaintenanceWindow" in data:
        out["maintenance_window"] = data["MaintenanceWindow"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "TLSEnabled" in data:
        out["tls_enabled"] = data["TLSEnabled"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "SnapshotArns" in data:
        import aws_sdk_memorydb.types.snapshot_arns_list

        out["snapshot_arns"] = (
            aws_sdk_memorydb.types.snapshot_arns_list.deserialize_aws_json_1_1(
                data["SnapshotArns"]
            )
        )
    if "SnapshotName" in data:
        out["snapshot_name"] = data["SnapshotName"]
    if "SnapshotRetentionLimit" in data:
        out["snapshot_retention_limit"] = data["SnapshotRetentionLimit"]
    if "Tags" in data:
        import aws_sdk_memorydb.types.tag_list

        out["tags"] = aws_sdk_memorydb.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "SnapshotWindow" in data:
        out["snapshot_window"] = data["SnapshotWindow"]
    if "ACLName" in data:
        out["acl_name"] = data["ACLName"]
    else:
        raise DeserializationError("CreateClusterRequest.acl_name required")
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "AutoMinorVersionUpgrade" in data:
        out["auto_minor_version_upgrade"] = data["AutoMinorVersionUpgrade"]
    if "DataTiering" in data:
        out["data_tiering"] = data["DataTiering"]
    if "NetworkType" in data:
        import aws_sdk_memorydb.types.network_type

        out["network_type"] = (
            aws_sdk_memorydb.types.network_type.deserialize_aws_json_1_1(
                data["NetworkType"]
            )
        )
    if "IpDiscovery" in data:
        import aws_sdk_memorydb.types.ip_discovery

        out["ip_discovery"] = (
            aws_sdk_memorydb.types.ip_discovery.deserialize_aws_json_1_1(
                data["IpDiscovery"]
            )
        )
    return out
