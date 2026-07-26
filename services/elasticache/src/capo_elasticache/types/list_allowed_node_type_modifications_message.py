"""Generated from Smithy shape ``com.amazonaws.elasticache#ListAllowedNodeTypeModificationsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.string


class ListAllowedNodeTypeModificationsMessage(TypedDict, closed=True):
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cluster you want to scale up to a larger node instanced type. ElastiCache uses the cluster id to identify the current node type of this cluster and from that to create a list of node types you can scale up to.</p> <important> <p>You must provide a value for either the <code>CacheClusterId</code> or the <code>ReplicationGroupId</code>.</p> </important>"""
    replication_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the replication group want to scale up to a larger node type. ElastiCache uses the replication group id to identify the current node type being used by this replication group, and from that to create a list of node types you can scale up to.</p> <important> <p>You must provide a value for either the <code>CacheClusterId</code> or the <code>ReplicationGroupId</code>.</p> </important>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ListAllowedNodeTypeModificationsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "replication_group_id" in value:
        pairs.append(
            (f"{prefix}.ReplicationGroupId", str(value["replication_group_id"]))
        )


def deserialize_query(el: Element) -> ListAllowedNodeTypeModificationsMessage:
    out: ListAllowedNodeTypeModificationsMessage = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_replication_group_id = el.find("ReplicationGroupId")
    if child_replication_group_id is not None:
        out["replication_group_id"] = str(child_replication_group_id.text or "")
    return out
