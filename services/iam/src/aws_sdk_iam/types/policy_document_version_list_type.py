"""Generated from Smithy shape ``com.amazonaws.iam#policyDocumentVersionListType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.policy_version

policyDocumentVersionListType: TypeAlias = list[
    "aws_sdk_iam.types.policy_version.PolicyVersion"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: policyDocumentVersionListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.policy_version

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.policy_version.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> policyDocumentVersionListType:
    import aws_sdk_iam.types.policy_version

    out: policyDocumentVersionListType = []
    for child in el.findall("member"):
        out.append(aws_sdk_iam.types.policy_version.deserialize_query(child))
    return out


def serialize_query_flat(
    value: policyDocumentVersionListType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_iam.types.policy_version

    for n, item in enumerate(value, 1):
        aws_sdk_iam.types.policy_version.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> policyDocumentVersionListType:
    import aws_sdk_iam.types.policy_version

    out: policyDocumentVersionListType = []
    for child in parent.findall(tag):
        out.append(aws_sdk_iam.types.policy_version.deserialize_query(child))
    return out
