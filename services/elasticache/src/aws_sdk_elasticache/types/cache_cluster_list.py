"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheClusterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_cluster

CacheClusterList: TypeAlias = list[
    "aws_sdk_elasticache.types.cache_cluster.CacheCluster"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_cluster

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_cluster.serialize_query(
            item, pairs, f"{prefix}.CacheCluster.{n}"
        )


def deserialize_query(el: Element) -> CacheClusterList:
    import aws_sdk_elasticache.types.cache_cluster

    out: CacheClusterList = []
    for child in el.findall("CacheCluster"):
        out.append(aws_sdk_elasticache.types.cache_cluster.deserialize_query(child))
    return out


def serialize_query_flat(
    value: CacheClusterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_cluster

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_cluster.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CacheClusterList:
    import aws_sdk_elasticache.types.cache_cluster

    out: CacheClusterList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.cache_cluster.deserialize_query(child))
    return out
