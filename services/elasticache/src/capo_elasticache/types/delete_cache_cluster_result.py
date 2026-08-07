"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteCacheClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_cluster


class DeleteCacheClusterResult(TypedDict, closed=True):
    cache_cluster: NotRequired["capo_elasticache.types.cache_cluster.CacheCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteCacheClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_cluster" in value:
        import capo_elasticache.types.cache_cluster

        capo_elasticache.types.cache_cluster.serialize_query(
            value["cache_cluster"], pairs, f"{key_prefix}CacheCluster"
        )


def deserialize_query(el: Element) -> DeleteCacheClusterResult:
    out: DeleteCacheClusterResult = {}  # type: ignore[typeddict-item]
    child_cache_cluster = el.find("CacheCluster")
    if child_cache_cluster is not None:
        import capo_elasticache.types.cache_cluster

        out["cache_cluster"] = capo_elasticache.types.cache_cluster.deserialize_query(
            child_cache_cluster
        )
    return out
