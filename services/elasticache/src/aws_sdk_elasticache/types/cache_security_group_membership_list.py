"""Generated from Smithy shape ``com.amazonaws.elasticache#CacheSecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.cache_security_group_membership

CacheSecurityGroupMembershipList: TypeAlias = list[
    "aws_sdk_elasticache.types.cache_security_group_membership.CacheSecurityGroupMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CacheSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.CacheSecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> CacheSecurityGroupMembershipList:
    import aws_sdk_elasticache.types.cache_security_group_membership

    out: CacheSecurityGroupMembershipList = []
    for child in el.findall("CacheSecurityGroup"):
        out.append(
            aws_sdk_elasticache.types.cache_security_group_membership.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: CacheSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.cache_security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.cache_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> CacheSecurityGroupMembershipList:
    import aws_sdk_elasticache.types.cache_security_group_membership

    out: CacheSecurityGroupMembershipList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.cache_security_group_membership.deserialize_query(
                child
            )
        )
    return out
