"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSecurityGroups``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_security_group

CacheSecurityGroups: TypeAlias = list[
    "aws_sdk_elasticache.types.cache_security_group.CacheSecurityGroup"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSecurityGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_security_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_security_group.serialize_query(
            item, pairs, f"{prefix}.CacheSecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> CacheSecurityGroups:
    import aws_sdk_elasticache.types.cache_security_group

    out: CacheSecurityGroups = []
    for child in el.findall("CacheSecurityGroup"):
        out.append(
            aws_sdk_elasticache.types.cache_security_group.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: CacheSecurityGroups, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_security_group

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_security_group.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CacheSecurityGroups:
    import aws_sdk_elasticache.types.cache_security_group

    out: CacheSecurityGroups = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.cache_security_group.deserialize_query(child)
        )
    return out
