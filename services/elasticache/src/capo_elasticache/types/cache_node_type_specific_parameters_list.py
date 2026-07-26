"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheNodeTypeSpecificParametersList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_node_type_specific_parameter

CacheNodeTypeSpecificParametersList: TypeAlias = list[
    "capo_elasticache.types.cache_node_type_specific_parameter.CacheNodeTypeSpecificParameter"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheNodeTypeSpecificParametersList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_elasticache.types.cache_node_type_specific_parameter

    for n, item in enumerate(value, 1):
        capo_elasticache.types.cache_node_type_specific_parameter.serialize_query(
            item, pairs, f"{prefix}.CacheNodeTypeSpecificParameter.{n}"
        )


def deserialize_query(el: Element) -> CacheNodeTypeSpecificParametersList:
    import capo_elasticache.types.cache_node_type_specific_parameter

    out: CacheNodeTypeSpecificParametersList = []
    for child in el.findall("CacheNodeTypeSpecificParameter"):
        out.append(
            capo_elasticache.types.cache_node_type_specific_parameter.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: CacheNodeTypeSpecificParametersList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_elasticache.types.cache_node_type_specific_parameter

    for n, item in enumerate(value, 1):
        capo_elasticache.types.cache_node_type_specific_parameter.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> CacheNodeTypeSpecificParametersList:
    import capo_elasticache.types.cache_node_type_specific_parameter

    out: CacheNodeTypeSpecificParametersList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.cache_node_type_specific_parameter.deserialize_query(
                child
            )
        )
    return out
