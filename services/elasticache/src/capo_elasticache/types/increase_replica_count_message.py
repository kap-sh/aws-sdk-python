"""Generated from Smithy shape ``com.amazonaws.elasticache#IncreaseReplicaCountMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.boolean
    import capo_elasticache.types.integer_optional
    import capo_elasticache.types.replica_configuration_list
    import capo_elasticache.types.string


class IncreaseReplicaCountMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The id of the replication group to which you want to add replica nodes.</p>"""
    new_replica_count: NotRequired[
        "capo_elasticache.types.integer_optional.IntegerOptional"
    ]
    """<p>The number of read replica nodes you want at the completion of this operation. For Valkey or Redis OSS (cluster mode disabled) replication groups, this is the number of replica nodes in the replication group. For Valkey or Redis OSS (cluster mode enabled) replication groups, this is the number of replica nodes in each of the replication group's node groups.</p>"""
    replica_configuration: NotRequired[
        "capo_elasticache.types.replica_configuration_list.ReplicaConfigurationList"
    ]
    """<p>A list of <code>ConfigureShard</code> objects that can be used to configure each shard in a Valkey or Redis OSS (cluster mode enabled) replication group. The <code>ConfigureShard</code> has three members: <code>NewReplicaCount</code>, <code>NodeGroupId</code>, and <code>PreferredAvailabilityZones</code>.</p>"""
    apply_immediately: NotRequired["capo_elasticache.types.boolean.Boolean"]
    """<p>If <code>True</code>, the number of replica nodes is increased immediately. <code>ApplyImmediately=False</code> is not currently supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: IncreaseReplicaCountMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "new_replica_count" in value:
        pairs.append((f"{prefix}.NewReplicaCount", str(value["new_replica_count"])))
    if "replica_configuration" in value:
        import capo_elasticache.types.replica_configuration_list

        capo_elasticache.types.replica_configuration_list.serialize_query(
            value["replica_configuration"], pairs, f"{prefix}.ReplicaConfiguration"
        )
    if "apply_immediately" in value:
        pairs.append(
            (
                f"{prefix}.ApplyImmediately",
                "true" if value["apply_immediately"] else "false",
            )
        )


def deserialize_query(el: Element) -> IncreaseReplicaCountMessage:
    out: IncreaseReplicaCountMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_new_replica_count = el.find("NewReplicaCount")
    if child_new_replica_count is not None:
        out["new_replica_count"] = int(child_new_replica_count.text or "")
    child_replica_configuration = el.find("ReplicaConfiguration")
    if child_replica_configuration is not None:
        import capo_elasticache.types.replica_configuration_list

        out["replica_configuration"] = (
            capo_elasticache.types.replica_configuration_list.deserialize_query(
                child_replica_configuration
            )
        )
    child_apply_immediately = el.find("ApplyImmediately")
    if child_apply_immediately is not None:
        out["apply_immediately"] = (
            child_apply_immediately.text or ""
        ).lower() == "true"
    return out
