"""Generated from Smithy shape ``com.amazonaws.neptune#DBSecurityGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_security_group_membership

DBSecurityGroupMembershipList: TypeAlias = list[
    "aws_sdk_neptune.types.db_security_group_membership.DBSecurityGroupMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.db_security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.db_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.DBSecurityGroup.{n}"
        )


def deserialize_query(el: Element) -> DBSecurityGroupMembershipList:
    import aws_sdk_neptune.types.db_security_group_membership

    out: DBSecurityGroupMembershipList = []
    for child in el.findall("DBSecurityGroup"):
        out.append(
            aws_sdk_neptune.types.db_security_group_membership.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DBSecurityGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.db_security_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.db_security_group_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DBSecurityGroupMembershipList:
    import aws_sdk_neptune.types.db_security_group_membership

    out: DBSecurityGroupMembershipList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_neptune.types.db_security_group_membership.deserialize_query(child)
        )
    return out
