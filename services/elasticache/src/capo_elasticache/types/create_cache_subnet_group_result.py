"""Generated from Smithy shape ``com.amazonaws.elasticache#CreateCacheSubnetGroupResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.cache_subnet_group


class CreateCacheSubnetGroupResult(TypedDict, closed=True):
    cache_subnet_group: NotRequired[
        "capo_elasticache.types.cache_subnet_group.CacheSubnetGroup"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateCacheSubnetGroupResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_subnet_group" in value:
        import capo_elasticache.types.cache_subnet_group

        capo_elasticache.types.cache_subnet_group.serialize_query(
            value["cache_subnet_group"], pairs, f"{prefix}.CacheSubnetGroup"
        )


def deserialize_query(el: Element) -> CreateCacheSubnetGroupResult:
    out: CreateCacheSubnetGroupResult = {}  # type: ignore[typeddict-item]
    child_cache_subnet_group = el.find("CacheSubnetGroup")
    if child_cache_subnet_group is not None:
        import capo_elasticache.types.cache_subnet_group

        out["cache_subnet_group"] = (
            capo_elasticache.types.cache_subnet_group.deserialize_query(
                child_cache_subnet_group
            )
        )
    return out
