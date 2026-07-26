"""Generated from Smithy shape ``com.amazonaws.elasticache#ReservedCacheNodeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.reserved_cache_node

ReservedCacheNodeList: TypeAlias = list[
    "capo_elasticache.types.reserved_cache_node.ReservedCacheNode"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ReservedCacheNodeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.reserved_cache_node

    for n, item in enumerate(value, 1):
        capo_elasticache.types.reserved_cache_node.serialize_query(
            item, pairs, f"{prefix}.ReservedCacheNode.{n}"
        )


def deserialize_query(el: Element) -> ReservedCacheNodeList:
    import capo_elasticache.types.reserved_cache_node

    out: ReservedCacheNodeList = []
    for child in el.findall("ReservedCacheNode"):
        out.append(capo_elasticache.types.reserved_cache_node.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ReservedCacheNodeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.reserved_cache_node

    for n, item in enumerate(value, 1):
        capo_elasticache.types.reserved_cache_node.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ReservedCacheNodeList:
    import capo_elasticache.types.reserved_cache_node

    out: ReservedCacheNodeList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.reserved_cache_node.deserialize_query(child))
    return out
