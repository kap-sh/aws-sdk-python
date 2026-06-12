"""Generated from Smithy shape ``com.amazonaws.rds#OptionGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.option_group_membership

OptionGroupMembershipList: TypeAlias = list[
    "aws_sdk_rds.types.option_group_membership.OptionGroupMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_group_membership.serialize_query(
            item, pairs, f"{prefix}.OptionGroupMembership.{n}"
        )


def deserialize_query(el: Element) -> OptionGroupMembershipList:
    import aws_sdk_rds.types.option_group_membership

    out: OptionGroupMembershipList = []
    for child in el.findall("OptionGroupMembership"):
        out.append(aws_sdk_rds.types.option_group_membership.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.option_group_membership

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.option_group_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OptionGroupMembershipList:
    import aws_sdk_rds.types.option_group_membership

    out: OptionGroupMembershipList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.option_group_membership.deserialize_query(child))
    return out
