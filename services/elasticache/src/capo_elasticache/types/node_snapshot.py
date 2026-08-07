"""Generated from Smithy shape ``com.amazonaws.elasticache#NodeSnapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.node_group_configuration
    import capo_elasticache.types.string
    import capo_elasticache.types.t_stamp


class NodeSnapshot(TypedDict, closed=True):
    cache_cluster_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>A unique identifier for the source cluster.</p>"""
    node_group_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>A unique identifier for the source node group (shard).</p>"""
    cache_node_id: NotRequired["capo_elasticache.types.string.String"]
    """<p>The cache node identifier for the node in the source cluster.</p>"""
    node_group_configuration: NotRequired[
        "capo_elasticache.types.node_group_configuration.NodeGroupConfiguration"
    ]
    """<p>The configuration for the source node group (shard).</p>"""
    cache_size: NotRequired["capo_elasticache.types.string.String"]
    """<p>The size of the cache on the source cache node.</p>"""
    cache_node_create_time: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date and time when the cache node was created in the source cluster.</p>"""
    snapshot_create_time: NotRequired["capo_elasticache.types.t_stamp.TStamp"]
    """<p>The date and time when the source node's metadata and cache data set was obtained for the snapshot.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: NodeSnapshot, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_cluster_id" in value:
        pairs.append((f"{key_prefix}CacheClusterId", str(value["cache_cluster_id"])))
    if "node_group_id" in value:
        pairs.append((f"{key_prefix}NodeGroupId", str(value["node_group_id"])))
    if "cache_node_id" in value:
        pairs.append((f"{key_prefix}CacheNodeId", str(value["cache_node_id"])))
    if "node_group_configuration" in value:
        import capo_elasticache.types.node_group_configuration

        capo_elasticache.types.node_group_configuration.serialize_query(
            value["node_group_configuration"],
            pairs,
            f"{key_prefix}NodeGroupConfiguration",
        )
    if "cache_size" in value:
        pairs.append((f"{key_prefix}CacheSize", str(value["cache_size"])))
    if "cache_node_create_time" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["cache_node_create_time"], pairs, f"{key_prefix}CacheNodeCreateTime"
        )
    if "snapshot_create_time" in value:
        import capo_elasticache.types.t_stamp

        capo_elasticache.types.t_stamp.serialize_query(
            value["snapshot_create_time"], pairs, f"{key_prefix}SnapshotCreateTime"
        )


def deserialize_query(el: Element) -> NodeSnapshot:
    out: NodeSnapshot = {}  # type: ignore[typeddict-item]
    child_cache_cluster_id = el.find("CacheClusterId")
    if child_cache_cluster_id is not None:
        out["cache_cluster_id"] = str(child_cache_cluster_id.text or "")
    child_node_group_id = el.find("NodeGroupId")
    if child_node_group_id is not None:
        out["node_group_id"] = str(child_node_group_id.text or "")
    child_cache_node_id = el.find("CacheNodeId")
    if child_cache_node_id is not None:
        out["cache_node_id"] = str(child_cache_node_id.text or "")
    child_node_group_configuration = el.find("NodeGroupConfiguration")
    if child_node_group_configuration is not None:
        import capo_elasticache.types.node_group_configuration

        out["node_group_configuration"] = (
            capo_elasticache.types.node_group_configuration.deserialize_query(
                child_node_group_configuration
            )
        )
    child_cache_size = el.find("CacheSize")
    if child_cache_size is not None:
        out["cache_size"] = str(child_cache_size.text or "")
    child_cache_node_create_time = el.find("CacheNodeCreateTime")
    if child_cache_node_create_time is not None:
        import capo_elasticache.types.t_stamp

        out["cache_node_create_time"] = (
            capo_elasticache.types.t_stamp.deserialize_query(
                child_cache_node_create_time
            )
        )
    child_snapshot_create_time = el.find("SnapshotCreateTime")
    if child_snapshot_create_time is not None:
        import capo_elasticache.types.t_stamp

        out["snapshot_create_time"] = capo_elasticache.types.t_stamp.deserialize_query(
            child_snapshot_create_time
        )
    return out
