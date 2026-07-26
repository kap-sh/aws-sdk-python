"""Generated from Smithy shape ``com.amazonaws.iam#delegationRequestsListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.delegation_request

delegationRequestsListType: TypeAlias = list[
    "capo_iam.types.delegation_request.DelegationRequest"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: delegationRequestsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.delegation_request

    for n, item in enumerate(value, 1):
        capo_iam.types.delegation_request.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> delegationRequestsListType:
    import capo_iam.types.delegation_request

    out: delegationRequestsListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.delegation_request.deserialize_query(child))
    return out


def serialize_query_flat(
    value: delegationRequestsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.delegation_request

    for n, item in enumerate(value, 1):
        capo_iam.types.delegation_request.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> delegationRequestsListType:
    import capo_iam.types.delegation_request

    out: delegationRequestsListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.delegation_request.deserialize_query(child))
    return out
