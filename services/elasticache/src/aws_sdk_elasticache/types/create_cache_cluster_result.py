"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateCacheClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_cluster


class CreateCacheClusterResult(TypedDict, closed=True):
    cache_cluster: NotRequired["aws_sdk_elasticache.types.cache_cluster.CacheCluster"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCacheClusterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_cluster" in value:
        import aws_sdk_elasticache.types.cache_cluster

        aws_sdk_elasticache.types.cache_cluster.serialize_query(
            value["cache_cluster"], pairs, f"{prefix}.CacheCluster"
        )


def deserialize_query(el: Element) -> CreateCacheClusterResult:
    out: CreateCacheClusterResult = {}  # type: ignore[typeddict-item]
    child_cache_cluster = el.find("CacheCluster")
    if child_cache_cluster is not None:
        import aws_sdk_elasticache.types.cache_cluster

        out["cache_cluster"] = (
            aws_sdk_elasticache.types.cache_cluster.deserialize_query(
                child_cache_cluster
            )
        )
    return out
