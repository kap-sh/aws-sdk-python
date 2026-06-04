"""Generated from Smithy shape ``com.amazonaws.iam#ManagedPolicyDetailListType``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.managed_policy_detail

ManagedPolicyDetailListType: TypeAlias = list[
    "aws_sdk_iam.types.managed_policy_detail.ManagedPolicyDetail"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ManagedPolicyDetailListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.managed_policy_detail

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.managed_policy_detail.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> ManagedPolicyDetailListType:
    import aws_sdk_iam.types.managed_policy_detail

    out: ManagedPolicyDetailListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.managed_policy_detail.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ManagedPolicyDetailListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.managed_policy_detail

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.managed_policy_detail.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> ManagedPolicyDetailListType:
    import aws_sdk_iam.types.managed_policy_detail

    out: ManagedPolicyDetailListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.managed_policy_detail.deserialize_query(child))
    return out
