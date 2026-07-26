"""Generated from Smithy shape ``com.amazonaws.neptune#OptionGroupMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.option_group_membership

OptionGroupMembershipList: TypeAlias = list[
    "capo_neptune.types.option_group_membership.OptionGroupMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OptionGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.option_group_membership

    for n, item in enumerate(value, 1):
        capo_neptune.types.option_group_membership.serialize_query(
            item, pairs, f"{prefix}.OptionGroupMembership.{n}"
        )


def deserialize_query(el: Element) -> OptionGroupMembershipList:
    import capo_neptune.types.option_group_membership

    out: OptionGroupMembershipList = []
    for child in el.findall("OptionGroupMembership"):
        out.append(capo_neptune.types.option_group_membership.deserialize_query(child))
    return out


def serialize_query_flat(
    value: OptionGroupMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.option_group_membership

    for n, item in enumerate(value, 1):
        capo_neptune.types.option_group_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OptionGroupMembershipList:
    import capo_neptune.types.option_group_membership

    out: OptionGroupMembershipList = []
    for child in parent.findall(tag):
        out.append(capo_neptune.types.option_group_membership.deserialize_query(child))
    return out
