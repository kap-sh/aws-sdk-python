"""Generated from Smithy shape ``com.amazonaws.elasticache#SecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.security_group_membership

SecurityGroupMembershipList: TypeAlias = list[
    "aws_sdk_elasticache.types.security_group_membership.SecurityGroupMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.security_group_membership.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> SecurityGroupMembershipList:
    import aws_sdk_elasticache.types.security_group_membership

    out: SecurityGroupMembershipList = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_elasticache.types.security_group_membership.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: SecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_elasticache.types.security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_elasticache.types.security_group_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> SecurityGroupMembershipList:
    import aws_sdk_elasticache.types.security_group_membership

    out: SecurityGroupMembershipList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_elasticache.types.security_group_membership.deserialize_query(child)
        )
    return out
