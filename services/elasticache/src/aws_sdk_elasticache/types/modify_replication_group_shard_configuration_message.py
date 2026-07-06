"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyReplicationGroupShardConfigurationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean
    import aws_sdk_elasticache.types.integer
    import aws_sdk_elasticache.types.node_groups_to_remove_list
    import aws_sdk_elasticache.types.node_groups_to_retain_list
    import aws_sdk_elasticache.types.resharding_configuration_list
    import aws_sdk_elasticache.types.string


class ModifyReplicationGroupShardConfigurationMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the Valkey or Redis OSS (cluster mode enabled) cluster (replication group) on which the shards are to be configured.</p>"""
    node_group_count: NotRequired["aws_sdk_elasticache.types.integer.Integer"]
    """<p>The number of node groups (shards) that results from the modification of the shard configuration.</p>"""
    apply_immediately: NotRequired["aws_sdk_elasticache.types.boolean.Boolean"]
    """<p>Indicates that the shard reconfiguration process begins immediately. At present, the only permitted value for this parameter is <code>true</code>.</p> <p>Value: true</p>"""
    resharding_configuration: NotRequired[
        "aws_sdk_elasticache.types.resharding_configuration_list.ReshardingConfigurationList"
    ]
    """<p>Specifies the preferred availability zones for each node group in the cluster. If the value of <code>NodeGroupCount</code> is greater than the current number of node groups (shards), you can use this parameter to specify the preferred availability zones of the cluster's shards. If you omit this parameter ElastiCache selects availability zones for you.</p> <p>You can specify this parameter only if the value of <code>NodeGroupCount</code> is greater than the current number of node groups (shards).</p>"""
    node_groups_to_remove: NotRequired[
        "aws_sdk_elasticache.types.node_groups_to_remove_list.NodeGroupsToRemoveList"
    ]
    """<p>If the value of <code>NodeGroupCount</code> is less than the current number of node groups (shards), then either <code>NodeGroupsToRemove</code> or <code>NodeGroupsToRetain</code> is required. <code>NodeGroupsToRemove</code> is a list of <code>NodeGroupId</code>s to remove from the cluster.</p> <p>ElastiCache will attempt to remove all node groups listed by <code>NodeGroupsToRemove</code> from the cluster.</p>"""
    node_groups_to_retain: NotRequired[
        "aws_sdk_elasticache.types.node_groups_to_retain_list.NodeGroupsToRetainList"
    ]
    """<p>If the value of <code>NodeGroupCount</code> is less than the current number of node groups (shards), then either <code>NodeGroupsToRemove</code> or <code>NodeGroupsToRetain</code> is required. <code>NodeGroupsToRetain</code> is a list of <code>NodeGroupId</code>s to retain in the cluster.</p> <p>ElastiCache will attempt to remove all node groups except those listed by <code>NodeGroupsToRetain</code> from the cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyReplicationGroupShardConfigurationMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "node_group_count" in value:
        pairs.append((f"{prefix}.NodeGroupCount", str(value["node_group_count"])))
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )
    if "resharding_configuration" in value:
        import aws_sdk_elasticache.types.resharding_configuration_list

        aws_sdk_elasticache.types.resharding_configuration_list.serialize_query(
            value["resharding_configuration"],
            pairs,
            f"{prefix}.ReshardingConfiguration",
        )
    if "node_groups_to_remove" in value:
        import aws_sdk_elasticache.types.node_groups_to_remove_list

        aws_sdk_elasticache.types.node_groups_to_remove_list.serialize_query(
            value["node_groups_to_remove"], pairs, f"{prefix}.NodeGroupsToRemove"
        )
    if "node_groups_to_retain" in value:
        import aws_sdk_elasticache.types.node_groups_to_retain_list

        aws_sdk_elasticache.types.node_groups_to_retain_list.serialize_query(
            value["node_groups_to_retain"], pairs, f"{prefix}.NodeGroupsToRetain"
        )


def deserialize_query(el: Element) -> ModifyReplicationGroupShardConfigurationMessage:
    out: ModifyReplicationGroupShardConfigurationMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_node_group_count = el.find("NodeGroupCount")
    if child_node_group_count is not None:
        out["node_group_count"] = int(child_node_group_count.text or "")
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    child_resharding_configuration = el.find("ReshardingConfiguration")
    if child_resharding_configuration is not None:
        import aws_sdk_elasticache.types.resharding_configuration_list

        out["resharding_configuration"] = (
            aws_sdk_elasticache.types.resharding_configuration_list.deserialize_query(
                child_resharding_configuration
            )
        )
    child_node_groups_to_remove = el.find("NodeGroupsToRemove")
    if child_node_groups_to_remove is not None:
        import aws_sdk_elasticache.types.node_groups_to_remove_list

        out["node_groups_to_remove"] = (
            aws_sdk_elasticache.types.node_groups_to_remove_list.deserialize_query(
                child_node_groups_to_remove
            )
        )
    child_node_groups_to_retain = el.find("NodeGroupsToRetain")
    if child_node_groups_to_retain is not None:
        import aws_sdk_elasticache.types.node_groups_to_retain_list

        out["node_groups_to_retain"] = (
            aws_sdk_elasticache.types.node_groups_to_retain_list.deserialize_query(
                child_node_groups_to_retain
            )
        )
    return out
