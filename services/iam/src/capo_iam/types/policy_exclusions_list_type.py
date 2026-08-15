"""Generated from Smithy shape ``com.amazonaws.iam#PolicyExclusionsListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_identifier

PolicyExclusionsListType: TypeAlias = list[
    "capo_iam.types.policy_identifier.PolicyIdentifier"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyExclusionsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.policy_identifier

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.policy_identifier.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PolicyExclusionsListType:
    import capo_iam.types.policy_identifier

    out: PolicyExclusionsListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.policy_identifier.deserialize_query(child))
    return out


def serialize_query_flat(
    value: PolicyExclusionsListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.policy_identifier

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_iam.types.policy_identifier.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> PolicyExclusionsListType:
    import capo_iam.types.policy_identifier

    out: PolicyExclusionsListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.policy_identifier.deserialize_query(child))
    return out
