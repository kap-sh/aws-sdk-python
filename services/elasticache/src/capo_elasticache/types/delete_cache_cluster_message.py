"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteCacheClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class DeleteCacheClusterMessage(TypedDict, closed=True):
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cluster identifier for the cluster to be deleted. This parameter is not case sensitive.</p>"""
    final_snapshot_identifier: NotRequired["capo_elasticache.types.string.String"]
    """<p>The user-supplied name of a final cluster snapshot. This is the unique name that identifies the snapshot. ElastiCache creates the snapshot, and then deletes the cluster immediately afterward.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCacheClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_cluster_id" in value:
        pairs.append((f"{key_prefix}CacheClusterId", str(value["cache_cluster_id"])))
    if "final_snapshot_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}FinalSnapshotIdentifier",
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
