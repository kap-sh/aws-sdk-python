"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_cluster_list
    import aws_sdk_elasticache.types.string


class CacheClusterMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>Provides an identifier to allow retrieval of paginated results.</p>"""
    cache_clusters: NotRequired[
        "aws_sdk_elasticache.types.cache_cluster_list.CacheClusterList"
    ]
    """<p>A list of clusters. Each item in the list contains detailed information about one cluster.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "cache_clusters" in value:
        import aws_sdk_elasticache.types.cache_cluster_list

        aws_sdk_elasticache.types.cache_cluster_list.serialize_query(
            value["cache_clusters"], pairs, f"{prefix}.CacheClusters"
        )


def deserialize_query(el: Element) -> CacheClusterMessage:
    out: CacheClusterMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_cache_clusters = el.find("CacheClusters")
    if child_cache_clusters is not None:
        import aws_sdk_elasticache.types.cache_cluster_list

        out["cache_clusters"] = (
            aws_sdk_elasticache.types.cache_cluster_list.deserialize_query(
                child_cache_clusters
            )
        )
    return out
