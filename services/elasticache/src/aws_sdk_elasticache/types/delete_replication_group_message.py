"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteReplicationGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean_optional
    import aws_sdk_elasticache.types.string


class DeleteReplicationGroupMessage(TypedDict, closed=True):
    replication_group_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The identifier for the cluster to be deleted. This parameter is not case sensitive.</p>"""
    retain_primary_cluster: NotRequired[
        "aws_sdk_elasticache.types.boolean_optional.BooleanOptional"
    ]
    """<p>If set to <code>true</code>, all of the read replicas are deleted, but the primary node is retained.</p>"""
    final_snapshot_identifier: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of a final node group (shard) snapshot. ElastiCache creates the snapshot from the primary node in the cluster, rather than one of the replicas; this is to ensure that it captures the freshest data. After the final snapshot is taken, the replication group is immediately deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteReplicationGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )
    if "retain_primary_cluster" in value:
        pairs.append(
            (
                f"{prefix}.RetainPrimaryCluster",
                "true" if value["retain_primary_cluster"] else "false",
            )
        )
    if "final_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.FinalSnapshotIdentifier",
                str(value["final_snapshot_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteReplicationGroupMessage:
    out: DeleteReplicationGroupMessage = {}  # type: ignore[typeddict-item]
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    child_retain_primary_cluster = el.find("RetainPrimaryCluster")
    if child_retain_primary_cluster is not None:
        out["retain_primary_cluster"] = (
            child_retain_primary_cluster.text or ""
        ).lower() == "true"
    child_final_snapshot_identifier = el.find("FinalSnapshotIdentifier")
    if child_final_snapshot_identifier is not None:
        out["final_snapshot_identifier"] = str(
            child_final_snapshot_identifier.text or ""
        )
    return out
