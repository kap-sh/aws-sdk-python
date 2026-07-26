"""Generated from Smithy shape ``com.amazonaws.iam#PolicyUserListType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.policy_user

PolicyUserListType: TypeAlias = list["capo_iam.types.policy_user.PolicyUser"]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyUserListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.policy_user

    for n, item in enumerate(value, 1):
        capo_iam.types.policy_user.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> PolicyUserListType:
    import capo_iam.types.policy_user

    out: PolicyUserListType = []
    for child in el.findall("member"):
        out.append(capo_iam.types.policy_user.deserialize_query(child))
    return out


def serialize_query_flat(
    value: PolicyUserListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.policy_user

    for n, item in enumerate(value, 1):
        capo_iam.types.policy_user.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> PolicyUserListType:
    import capo_iam.types.policy_user

    out: PolicyUserListType = []
    for child in parent.findall(tag):
        out.append(capo_iam.types.policy_user.deserialize_query(child))
    return out
