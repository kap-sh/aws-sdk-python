"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheNodeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_node

CacheNodeList: TypeAlias = list["aws_sdk_elasticache.types.cache_node.CacheNode"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheNodeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_node

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_node.serialize_query(
            item, pairs, f"{prefix}.CacheNode.{n}"
        )


def deserialize_query(el: Element) -> CacheNodeList:
    import aws_sdk_elasticache.types.cache_node

    out: CacheNodeList = []
    for child in el.findall("CacheNode"):
        out.append(aws_sdk_elasticache.types.cache_node.deserialize_query(child))
    return out


def serialize_query_flat(
    value: CacheNodeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_node

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_node.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CacheNodeList:
    import aws_sdk_elasticache.types.cache_node

    out: CacheNodeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_elasticache.types.cache_node.deserialize_query(child))
    return out
