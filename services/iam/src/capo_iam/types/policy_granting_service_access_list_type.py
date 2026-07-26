"""Generated from Smithy shape ``com.amazonaws.iam#policyGrantingServiceAccessListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_granting_service_access

policyGrantingServiceAccessListType: TypeAlias = list[
    "capo_iam.types.policy_granting_service_access.PolicyGrantingServiceAccess"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: policyGrantingServiceAccessListType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_iam.types.policy_granting_service_access

    for n, item in enumerate(value, 1):
        capo_iam.types.policy_granting_service_access.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> policyGrantingServiceAccessListType:
    import capo_iam.types.policy_granting_service_access

    out: policyGrantingServiceAccessListType = []
    for child in el.findall("member"):
        out.append(
            capo_iam.types.policy_granting_service_access.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: policyGrantingServiceAccessListType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_iam.types.policy_granting_service_access

    for n, item in enumerate(value, 1):
        capo_iam.types.policy_granting_service_access.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> policyGrantingServiceAccessListType:
    import capo_iam.types.policy_granting_service_access

    out: policyGrantingServiceAccessListType = []
    for child in parent.findall(tag):
        out.append(
            capo_iam.types.policy_granting_service_access.deserialize_query(child)
        )
    return out
