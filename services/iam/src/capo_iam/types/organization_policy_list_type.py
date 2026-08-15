"""Generated from Smithy shape ``com.amazonaws.iam#OrganizationPolicyListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.ordered_organization_policy_type

OrganizationPolicyListType: TypeAlias = list[
    "capo_iam.types.ordered_organization_policy_type.OrderedOrganizationPolicyType"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: OrganizationPolicyListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.ordered_organization_policy_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.ordered_organization_policy_type.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> OrganizationPolicyListType:
    import capo_iam.types.ordered_organization_policy_type

    out: OrganizationPolicyListType = []
    for child in el.findall("member"):
        out.append(
            capo_iam.types.ordered_organization_policy_type.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: OrganizationPolicyListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.ordered_organization_policy_type

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.ordered_organization_policy_type.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> OrganizationPolicyListType:
    import capo_iam.types.ordered_organization_policy_type

    out: OrganizationPolicyListType = []
    for child in parent.findall(tag):
        out.append(
            capo_iam.types.ordered_organization_policy_type.deserialize_query(child)
        )
    return out
