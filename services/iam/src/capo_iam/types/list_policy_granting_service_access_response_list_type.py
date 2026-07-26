"""Generated from Smithy shape ``com.amazonaws.iam#listPolicyGrantingServiceAccessResponseListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.list_policies_granting_service_access_entry

listPolicyGrantingServiceAccessResponseListType: TypeAlias = list[
    "capo_iam.types.list_policies_granting_service_access_entry.ListPoliciesGrantingServiceAccessEntry"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: listPolicyGrantingServiceAccessResponseListType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_iam.types.list_policies_granting_service_access_entry

    for n, item in enumerate(value, 1):
        capo_iam.types.list_policies_granting_service_access_entry.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> listPolicyGrantingServiceAccessResponseListType:
    import capo_iam.types.list_policies_granting_service_access_entry

    out: listPolicyGrantingServiceAccessResponseListType = []
    for child in el.findall("member"):
        out.append(
            capo_iam.types.list_policies_granting_service_access_entry.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: listPolicyGrantingServiceAccessResponseListType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_iam.types.list_policies_granting_service_access_entry

    for n, item in enumerate(value, 1):
        capo_iam.types.list_policies_granting_service_access_entry.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> listPolicyGrantingServiceAccessResponseListType:
    import capo_iam.types.list_policies_granting_service_access_entry

    out: listPolicyGrantingServiceAccessResponseListType = []
    for child in parent.findall(tag):
        out.append(
            capo_iam.types.list_policies_granting_service_access_entry.deserialize_query(
                child
            )
        )
    return out
