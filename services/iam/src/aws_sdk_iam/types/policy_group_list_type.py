"""Generated from Smithy shape ``com.amazonaws.iam#PolicyGroupListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_group

PolicyGroupListType: TypeAlias = list["aws_sdk_iam.types.policy_group.PolicyGroup"]


# --- awsQuery ser/de ---
def serialize_query(
    value: PolicyGroupListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.policy_group

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.policy_group.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PolicyGroupListType:
    import aws_sdk_iam.types.policy_group

    out: PolicyGroupListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.policy_group.deserialize_query(child))
    return out


def serialize_query_flat(
    value: PolicyGroupListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.policy_group

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.policy_group.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> PolicyGroupListType:
    import aws_sdk_iam.types.policy_group

    out: PolicyGroupListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.policy_group.deserialize_query(child))
    return out
