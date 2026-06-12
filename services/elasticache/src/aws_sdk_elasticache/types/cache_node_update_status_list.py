"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheNodeUpdateStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_node_update_status

CacheNodeUpdateStatusList: TypeAlias = list[
    "aws_sdk_elasticache.types.cache_node_update_status.CacheNodeUpdateStatus"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheNodeUpdateStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_node_update_status

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_node_update_status.serialize_query(
            item, pairs, f"{prefix}.CacheNodeUpdateStatus.{n}"
        )


def deserialize_query(el: Element) -> CacheNodeUpdateStatusList:
    import aws_sdk_elasticache.types.cache_node_update_status

    out: CacheNodeUpdateStatusList = []
    for child in el.findall("CacheNodeUpdateStatus"):
        out.append(
            aws_sdk_elasticache.types.cache_node_update_status.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CacheNodeUpdateStatusList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_node_update_status

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_node_update_status.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CacheNodeUpdateStatusList:
    import aws_sdk_elasticache.types.cache_node_update_status

    out: CacheNodeUpdateStatusList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.cache_node_update_status.deserialize_query(child)
        )
    return out
