"""Generated from Smithy shape ``com.amazonaws.iam#attachedPoliciesListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.attached_policy

attachedPoliciesListType: TypeAlias = list[
    "capo_iam.types.attached_policy.AttachedPolicy"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: attachedPoliciesListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.attached_policy

    for n, item in enumerate(value, 1):
        capo_iam.types.attached_policy.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> attachedPoliciesListType:
    import capo_iam.types.attached_policy

    out: attachedPoliciesListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.attached_policy.deserialize_query(child))
    return out


def serialize_query_flat(
    value: attachedPoliciesListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.attached_policy

    for n, item in enumerate(value, 1):
        capo_iam.types.attached_policy.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> attachedPoliciesListType:
    import capo_iam.types.attached_policy

    out: attachedPoliciesListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.attached_policy.deserialize_query(child))
    return out
