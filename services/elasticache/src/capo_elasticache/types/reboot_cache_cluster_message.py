"""Generated from Smithy shape ``com.amazonaws.elasticache#RebootCacheClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_node_ids_list
    import capo_elasticache.types.string


class RebootCacheClusterMessage(TypedDict, closed=True):
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cluster identifier. This parameter is stored as a lowercase string.</p>"""
    cache_node_ids_to_reboot: NotRequired[
        "capo_elasticache.types.cache_node_ids_list.CacheNodeIdsList"
    ]
    """<p>A list of cache node IDs to reboot. A node ID is a numeric identifier (0001, 0002, etc.). To reboot an entire cluster, specify all of the cache node IDs.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RebootCacheClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_cluster_id" in value:
        pairs.append((f"{prefix}.CacheClusterId", str(value["cache_cluster_id"])))
    if "cache_node_ids_to_reboot" in value:
        import capo_elasticache.types.cache_node_ids_list

        capo_elasticache.types.cache_node_ids_list.serialize_query(
            value["cache_node_ids_to_reboot"], pairs, f"{prefix}.CacheNodeIdsToReboot"
        )


def deserialize_query(el: Element) -> RebootCacheClusterMessage:
    out: RebootCacheClusterMessage = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_cache_node_ids_to_reboot = el.find("CacheNodeIdsToReboot")
    if child_cache_node_ids_to_reboot is not None:
        import capo_elasticache.types.cache_node_ids_list

        out["cache_node_ids_to_reboot"] = (
            capo_elasticache.types.cache_node_ids_list.deserialize_query(
                child_cache_node_ids_to_reboot
            )
        )
    return out
