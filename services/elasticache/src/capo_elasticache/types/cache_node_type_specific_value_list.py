"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheNodeTypeSpecificValueList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_node_type_specific_value

CacheNodeTypeSpecificValueList: TypeAlias = list[
    "capo_elasticache.types.cache_node_type_specific_value.CacheNodeTypeSpecificValue"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheNodeTypeSpecificValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.cache_node_type_specific_value

    for n, item in enumerate(value, 1):
        capo_elasticache.types.cache_node_type_specific_value.serialize_query(
            item, pairs, f"{prefix}.CacheNodeTypeSpecificValue.{n}"
        )


def deserialize_query(el: Element) -> CacheNodeTypeSpecificValueList:
    import capo_elasticache.types.cache_node_type_specific_value

    out: CacheNodeTypeSpecificValueList = []
    for child in el.findall("CacheNodeTypeSpecificValue"):
        out.append(
            capo_elasticache.types.cache_node_type_specific_value.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: CacheNodeTypeSpecificValueList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.cache_node_type_specific_value

    for n, item in enumerate(value, 1):
        capo_elasticache.types.cache_node_type_specific_value.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CacheNodeTypeSpecificValueList:
    import capo_elasticache.types.cache_node_type_specific_value

    out: CacheNodeTypeSpecificValueList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.cache_node_type_specific_value.deserialize_query(
                child
            )
        )
    return out
