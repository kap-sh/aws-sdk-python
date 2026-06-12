"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteCacheClusterMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class DeleteCacheClusterMessage(TypedDict):
    cache_cluster_id: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The cluster identifier for the cluster to be deleted. This parameter is not case sensitive.</p>"""
    final_snapshot_identifier: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCacheClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "final_snapshot_identifier" in value:
        pairs.append(
            (
                f"{prefix}.FinalSnapshotIdentifier",
                str(value["final_snapshot_identifier"]),
            )
        )


def deserialize_query(el: Element) -> DeleteCacheClusterMessage:
    out: DeleteCacheClusterMessage = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_final_snapshot_identifier = el.find("FinalSnapshotIdentifier")
    if child_final_snapshot_identifier is not None:
        out["final_snapshot_identifier"] = str(
            child_final_snapshot_identifier.text or ""
        )
    return out
