"""Generated from Smithy shape ``com.amazonaws.iam#policyDetailListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_detail

policyDetailListType: TypeAlias = list["capo_iam.types.policy_detail.PolicyDetail"]


# --- awsQuery ser/de ---
def serialize_query(
    value: policyDetailListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.policy_detail

    for n, item in enumerate(value, 1):
        capo_iam.types.policy_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> policyDetailListType:
    import capo_iam.types.policy_detail

    out: policyDetailListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.policy_detail.deserialize_query(child))
    return out


def serialize_query_flat(
    value: policyDetailListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.policy_detail

    for n, item in enumerate(value, 1):
        capo_iam.types.policy_detail.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> policyDetailListType:
    import capo_iam.types.policy_detail

    out: policyDetailListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.policy_detail.deserialize_query(child))
    return out
