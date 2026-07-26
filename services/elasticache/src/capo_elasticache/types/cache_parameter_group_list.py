"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheParameterGroupList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_parameter_group

CacheParameterGroupList: TypeAlias = list[
    "capo_elasticache.types.cache_parameter_group.CacheParameterGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.cache_parameter_group

    for n, item in enumerate(value, 1):
        capo_elasticache.types.cache_parameter_group.serialize_query(
            item, pairs, f"{prefix}.CacheParameterGroup.{n}"
        )


def deserialize_query(el: Element) -> CacheParameterGroupList:
    import capo_elasticache.types.cache_parameter_group

    out: CacheParameterGroupList = []
    for child in el.findall("CacheParameterGroup"):
        out.append(
            capo_elasticache.types.cache_parameter_group.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CacheParameterGroupList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_elasticache.types.cache_parameter_group

    for n, item in enumerate(value, 1):
        capo_elasticache.types.cache_parameter_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CacheParameterGroupList:
    import capo_elasticache.types.cache_parameter_group

    out: CacheParameterGroupList = []
    for child in parent.findall(tag):
        out.append(
            capo_elasticache.types.cache_parameter_group.deserialize_query(child)
        )
    return out
