"""Generated from Smithy shape ``com.amazonaws.elasticache#DecreaseReplicaCountMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean
    import aws_sdk_elasticache.types.integer_optional
    import aws_sdk_elasticache.types.remove_replicas_list
    import aws_sdk_elasticache.types.replica_configuration_list
    import aws_sdk_elasticache.types.string


class DecreaseReplicaCountMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The id of the replication group from which you want to remove replica nodes.</p>"""
    new_replica_count: NotRequired[
        "aws_sdk_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of read replica nodes you want at the completion of this operation. For Valkey or Redis OSS (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group. For Valkey or Redis OSS (cluster mode enabled) replication groups, this is the number of replica nodes in each of the replication group's node groups.</p> <p>The minimum number of replicas in a shard or replication group is:</p> <ul> <li> <p>Valkey or Redis OSS (cluster mode disabled)</p> <ul> <li> <p>If Multi-AZ is enabled: 1</p> </li> <li> <p>If Multi-AZ is not enabled: 0</p> </li> </ul> </li> <li> <p>Valkey or Redis OSS (cluster mode enabled): 0 (though you will not be able to failover to a replica if your primary node fails)</p> </li> </ul>"""
    replica_configuration: NotRequired[
        "aws_sdk_elasticache.types.replica_configuration_list.ReplicaConfigurationList"
    ]
    """<p>A list of <code>ConfigureShard</code> objects that can be used to configure each shard in a Valkey or Redis OSS replication group. The <code>ConfigureShard</code> has three members: <code>NewReplicaCount</code>, <code>NodeGroupId</code>, and <code>PreferredAvailabilityZones</code>.</p>"""
    replicas_to_remove: NotRequired[
        "aws_sdk_elasticache.types.remove_replicas_list.RemoveReplicasList"
    ]
    """<p>A list of the node ids to remove from the replication group or node group (shard).</p>"""
    apply_immediately: NotRequired["aws_sdk_elasticache.types.boolean.Boolean"]
    """<p>If <code>True</code>, the number of replica nodes is decreased immediately. <code>ApplyImmediately=False</code> is not currently supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DecreaseReplicaCountMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "new_replica_count" in value:
        pairs.append((f"{prefix}.NewReplicaCount", str(value["new_replica_count"])))
    if "replica_configuration" in value:
        import aws_sdk_elasticache.types.replica_configuration_list

        aws_sdk_elasticache.types.replica_configuration_list.serialize_query(
            value["replica_configuration"], pairs, f"{prefix}.ReplicaConfiguration"
        )
    if "replicas_to_remove" in value:
        import aws_sdk_elasticache.types.remove_replicas_list

        aws_sdk_elasticache.types.remove_replicas_list.serialize_query(
            value["replicas_to_remove"], pairs, f"{prefix}.ReplicasToRemove"
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )


def deserialize_query(el: Element) -> DecreaseReplicaCountMessage:
    out: DecreaseReplicaCountMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_new_replica_count = el.find("NewReplicaCount")
    if child_new_replica_count is not None:
        out["new_replica_count"] = int(child_new_replica_count.text or "")
    child_replica_configuration = el.find("ReplicaConfiguration")
    if child_replica_configuration is not None:
        import aws_sdk_elasticache.types.replica_configuration_list

        out["replica_configuration"] = (
            aws_sdk_elasticache.types.replica_configuration_list.deserialize_query(
                child_replica_configuration
            )
        )
    child_replicas_to_remove = el.find("ReplicasToRemove")
    if child_replicas_to_remove is not None:
        import aws_sdk_elasticache.types.remove_replicas_list

        out["replicas_to_remove"] = (
            aws_sdk_elasticache.types.remove_replicas_list.deserialize_query(
                child_replicas_to_remove
            )
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    return out
