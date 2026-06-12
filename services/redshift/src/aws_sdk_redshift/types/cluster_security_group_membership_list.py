"""Generated from Smithy shape ``com.amazonaws.redshift#ClusterSecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.cluster_security_group_membership

ClusterSecurityGroupMembershipList: TypeAlias = list[
    "aws_sdk_redshift.types.cluster_security_group_membership.ClusterSecurityGroupMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ClusterSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.cluster_security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.cluster_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.ClusterSecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> ClusterSecurityGroupMembershipList:
    import aws_sdk_redshift.types.cluster_security_group_membership

    out: ClusterSecurityGroupMembershipList = []
    for child in el.findall("ClusterSecurityGroup"):
        out.append(
            aws_sdk_redshift.types.cluster_security_group_membership.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: ClusterSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.cluster_security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.cluster_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> ClusterSecurityGroupMembershipList:
    import aws_sdk_redshift.types.cluster_security_group_membership

    out: ClusterSecurityGroupMembershipList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_redshift.types.cluster_security_group_membership.deserialize_query(
                child
            )
        )
    return out
