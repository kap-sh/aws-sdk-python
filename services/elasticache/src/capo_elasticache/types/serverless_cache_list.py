"""Generated from Smithy shape ``com.amazonaws.elasticache#ServerlessCacheList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.serverless_cache

ServerlessCacheList: TypeAlias = list[
    "capo_elasticache.types.serverless_cache.ServerlessCache"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ServerlessCacheList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.serverless_cache

    for n, item in enumerate(value, 1):
        capo_elasticache.types.serverless_cache.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ServerlessCacheList:
    import capo_elasticache.types.serverless_cache

    out: ServerlessCacheList = []
    for child in el.findall("member"):
        out.append(capo_elasticache.types.serverless_cache.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ServerlessCacheList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.serverless_cache

    for n, item in enumerate(value, 1):
        capo_elasticache.types.serverless_cache.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ServerlessCacheList:
    import capo_elasticache.types.serverless_cache

    out: ServerlessCacheList = []
    for child in parent.findall(tag):
        out.append(capo_elasticache.types.serverless_cache.deserialize_query(child))
    return out
