"""Generated from Smithy shape ``com.amazonaws.neptune#VpcSecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.vpc_security_group_membership

VpcSecurityGroupMembershipList: TypeAlias = list[
    "aws_sdk_neptune.types.vpc_security_group_membership.VpcSecurityGroupMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: VpcSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.vpc_security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.vpc_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.VpcSecurityGroupMembership.{n}"
        )


def deserialize_query(el: Element) -> VpcSecurityGroupMembershipList:
    import aws_sdk_neptune.types.vpc_security_group_membership

    out: VpcSecurityGroupMembershipList = []
    for child in el.findall("VpcSecurityGroupMembership"):
        out.append(
            aws_sdk_neptune.types.vpc_security_group_membership.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: VpcSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.vpc_security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.vpc_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> VpcSecurityGroupMembershipList:
    import aws_sdk_neptune.types.vpc_security_group_membership

    out: VpcSecurityGroupMembershipList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_neptune.types.vpc_security_group_membership.deserialize_query(child)
        )
    return out
