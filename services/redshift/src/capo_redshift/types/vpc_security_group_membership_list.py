"""Generated from Smithy shape ``com.amazonaws.redshift#VpcSecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.vpc_security_group_membership

VpcSecurityGroupMembershipList: TypeAlias = list[
    "capo_redshift.types.vpc_security_group_membership.VpcSecurityGroupMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: VpcSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.vpc_security_group_membership

    for n, item in enumerate(value, 1):
        capo_redshift.types.vpc_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.VpcSecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> VpcSecurityGroupMembershipList:
    import capo_redshift.types.vpc_security_group_membership

    out: VpcSecurityGroupMembershipList = []
    for child in el.findall("VpcSecurityGroup"):
        out.append(
            capo_redshift.types.vpc_security_group_membership.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: VpcSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.vpc_security_group_membership

    for n, item in enumerate(value, 1):
        capo_redshift.types.vpc_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> VpcSecurityGroupMembershipList:
    import capo_redshift.types.vpc_security_group_membership

    out: VpcSecurityGroupMembershipList = []
    for child in parent.findall(tag):
        out.append(
            capo_redshift.types.vpc_security_group_membership.deserialize_query(child)
        )
    return out
