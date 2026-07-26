"""Generated from Smithy shape ``com.amazonaws.neptune#DomainMembershipList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.domain_membership

DomainMembershipList: TypeAlias = list[
    "capo_neptune.types.domain_membership.DomainMembership"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DomainMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.domain_membership

    for n, item in enumerate(value, 1):
        capo_neptune.types.domain_membership.serialize_query(
            item, pairs, f"{prefix}.DomainMembership.{n}"
        )


def deserialize_query(el: Element) -> DomainMembershipList:
    import capo_neptune.types.domain_membership

    out: DomainMembershipList = []
    for child in el.findall("DomainMembership"):
        out.append(capo_neptune.types.domain_membership.deserialize_query(child))
    return out


def serialize_query_flat(
    value: DomainMembershipList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_neptune.types.domain_membership

    for n, item in enumerate(value, 1):
        capo_neptune.types.domain_membership.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DomainMembershipList:
    import capo_neptune.types.domain_membership

    out: DomainMembershipList = []
    for child in parent.findall(tag):
        out.append(capo_neptune.types.domain_membership.deserialize_query(child))
    return out
