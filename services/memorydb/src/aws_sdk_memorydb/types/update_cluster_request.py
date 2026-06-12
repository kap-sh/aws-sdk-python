"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.acl_name
    import aws_sdk_memorydb.types.integer_optional
    import aws_sdk_memorydb.types.ip_discovery
    import aws_sdk_memorydb.types.replica_configuration_request
    import aws_sdk_memorydb.types.security_group_ids_list
    import aws_sdk_memorydb.types.shard_configuration_request
    import aws_sdk_memorydb.types.string


class UpdateClusterRequest(TypedDict):
    cluster_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the cluster to update.</p>"""
    description: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The description of the cluster to update.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_memorydb.types.security_group_ids_list.SecurityGroupIdsList"
    ]
    """<p>The SecurityGroupIds to update.</p>"""
    maintenance_window: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>Specifies the weekly time range during which maintenance on the cluster is performed. It is specified as a range in the format ddd:hh24:mi-ddd:hh24:mi (24H Clock UTC). The minimum maintenance window is a 60 minute period.</p> <p>Valid values for <code>ddd</code> are:</p> <ul> <li> <p> <code>sun</code> </p> </li> <li> <p> <code>mon</code> </p> </li> <li> <p> <code>tue</code> </p> </li> <li> <p> <code>wed</code> </p> </li> <li> <p> <code>thu</code> </p> </li> <li> <p> <code>fri</code> </p> </li> <li> <p> <code>sat</code> </p> </li> </ul> <p>Example: <code>sun:23:00-mon:01:30</code> </p>"""
    sns_topic_arn: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The SNS topic ARN to update.</p>"""
    sns_topic_status: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The status of the Amazon SNS notification topic. Notifications are sent only if the status is active.</p>"""
    parameter_group_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the parameter group to update.</p>"""
    snapshot_window: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The daily time range (in UTC) during which MemoryDB begins taking a daily snapshot of your cluster.</p>"""
    snapshot_retention_limit: NotRequired[
        "aws_sdk_memorydb.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of days for which MemoryDB retains automatic cluster snapshots before deleting them. For example, if you set SnapshotRetentionLimit to 5, a snapshot that was taken today is retained for 5 days before being deleted.</p>"""
    node_type: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>A valid node type that you want to scale this cluster up or down to.</p>"""
    engine: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the engine to be used for the cluster.</p>"""
    engine_version: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The upgraded version of the engine to be run on the nodes. You can upgrade to a newer engine version, but you cannot downgrade to an earlier engine version. If you want to use an earlier engine version, you must delete the existing cluster and create it anew with the earlier engine version.</p>"""
    replica_configuration: NotRequired[
        "aws_sdk_memorydb.types.replica_configuration_request.ReplicaConfigurationRequest"
    ]
    """<p>The number of replicas that will reside in each shard.</p>"""
    shard_configuration: NotRequired[
        "aws_sdk_memorydb.types.shard_configuration_request.ShardConfigurationRequest"
    ]
    """<p>The number of shards in the cluster.</p>"""
    acl_name: NotRequired["aws_sdk_memorydb.types.acl_name.ACLName"]
    """<p>The Access Control List that is associated with the cluster.</p>"""
    ip_discovery: NotRequired["aws_sdk_memorydb.types.ip_discovery.IpDiscovery"]
    """<p>The mechanism for discovering IP addresses for the cluster discovery protocol. Valid values are 'ipv4' or 'ipv6'. When set to 'ipv4', cluster discovery functions such as cluster slots, cluster shards, and cluster nodes will return IPv4 addresses for cluster nodes. When set to 'ipv6', the cluster discovery functions return IPv6 addresses for cluster nodes. The value must be compatible with the NetworkType parameter. If not specified, the default is 'ipv4'.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "security_group_ids" in value:
        import aws_sdk_memorydb.types.security_group_ids_list

        out["SecurityGroupIds"] = (
            aws_sdk_memorydb.types.security_group_ids_list.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "maintenance_window" in value:
        out["MaintenanceWindow"] = value["maintenance_window"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    if "sns_topic_status" in value:
        out["SnsTopicStatus"] = value["sns_topic_status"]
    if "parameter_group_name" in value:
        out["ParameterGroupName"] = value["parameter_group_name"]
    if "snapshot_window" in value:
        out["SnapshotWindow"] = value["snapshot_window"]
    if "snapshot_retention_limit" in value:
        out["SnapshotRetentionLimit"] = value["snapshot_retention_limit"]
    if "node_type" in value:
        out["NodeType"] = value["node_type"]
    if "engine" in value:
        out["Engine"] = value["engine"]
    if "engine_version" in value:
        out["EngineVersion"] = value["engine_version"]
    if "replica_configuration" in value:
        import aws_sdk_memorydb.types.replica_configuration_request

        out["ReplicaConfiguration"] = (
            aws_sdk_memorydb.types.replica_configuration_request.serialize_aws_json_1_1(
                value["replica_configuration"]
            )
        )
    if "shard_configuration" in value:
        import aws_sdk_memorydb.types.shard_configuration_request

        out["ShardConfiguration"] = (
            aws_sdk_memorydb.types.shard_configuration_request.serialize_aws_json_1_1(
                value["shard_configuration"]
            )
        )
    if "acl_name" in value:
        out["ACLName"] = value["acl_name"]
    if "ip_discovery" in value:
        import aws_sdk_memorydb.types.ip_discovery

        out["IpDiscovery"] = aws_sdk_memorydb.types.ip_discovery.serialize_aws_json_1_1(
            value["ip_discovery"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterRequest:
    out: UpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError("UpdateClusterRequest.cluster_name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "SecurityGroupIds" in data:
        import aws_sdk_memorydb.types.security_group_ids_list

        out["security_group_ids"] = (
            aws_sdk_memorydb.types.security_group_ids_list.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "MaintenanceWindow" in data:
        out["maintenance_window"] = data["MaintenanceWindow"]
    if "SnsTopicArn" in data:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if "SnsTopicStatus" in data:
        out["sns_topic_status"] = data["SnsTopicStatus"]
    if "ParameterGroupName" in data:
        out["parameter_group_name"] = data["ParameterGroupName"]
    if "SnapshotWindow" in data:
        out["snapshot_window"] = data["SnapshotWindow"]
    if "SnapshotRetentionLimit" in data:
        out["snapshot_retention_limit"] = data["SnapshotRetentionLimit"]
    if "NodeType" in data:
        out["node_type"] = data["NodeType"]
    if "Engine" in data:
        out["engine"] = data["Engine"]
    if "EngineVersion" in data:
        out["engine_version"] = data["EngineVersion"]
    if "ReplicaConfiguration" in data:
        import aws_sdk_memorydb.types.replica_configuration_request

        out["replica_configuration"] = (
            aws_sdk_memorydb.types.replica_configuration_request.deserialize_aws_json_1_1(
                data["ReplicaConfiguration"]
            )
        )
    if "ShardConfiguration" in data:
        import aws_sdk_memorydb.types.shard_configuration_request

        out["shard_configuration"] = (
            aws_sdk_memorydb.types.shard_configuration_request.deserialize_aws_json_1_1(
                data["ShardConfiguration"]
            )
        )
    if "ACLName" in data:
        out["acl_name"] = data["ACLName"]
    if "IpDiscovery" in data:
        import aws_sdk_memorydb.types.ip_discovery

        out["ip_discovery"] = (
            aws_sdk_memorydb.types.ip_discovery.deserialize_aws_json_1_1(
                data["IpDiscovery"]
            )
        )
    return out
