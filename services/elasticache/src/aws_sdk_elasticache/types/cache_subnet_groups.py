"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSubnetGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_subnet_group

CacheSubnetGroups: TypeAlias = list[
    "aws_sdk_elasticache.types.cache_subnet_group.CacheSubnetGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSubnetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_subnet_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_subnet_group.serialize_query(
            item, pairs, f"{prefix}.CacheSubnetGroup.{n}"
        )


def deserialize_query(el: Element) -> CacheSubnetGroups:
    import aws_sdk_elasticache.types.cache_subnet_group

    out: CacheSubnetGroups = []
    for child in el.findall("CacheSubnetGroup"):
        out.append(
            aws_sdk_elasticache.types.cache_subnet_group.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CacheSubnetGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_subnet_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_subnet_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CacheSubnetGroups:
    import aws_sdk_elasticache.types.cache_subnet_group

    out: CacheSubnetGroups = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.cache_subnet_group.deserialize_query(child)
        )
    return out
