"""Generated from Smithy shape ``com.amazonaws.iam#PolicyIdentifierPolicyType``."""

from typing import Literal, TypeAlias, cast

from capo_iam._protocol.xml import Element

PolicyIdentifierPolicyType: TypeAlias = Literal[
    "inline",
    "aws-managed",
    "user-managed",
    "permission-boundary",
    "scp",
    "rcp",
]


# --- awsQuery ser/de ---
def to_query_text(value: PolicyIdentifierPolicyType) -> str:
    return value


def from_query_text(text: str) -> PolicyIdentifierPolicyType:
    return cast(PolicyIdentifierPolicyType, text)


def serialize_query(
    value: PolicyIdentifierPolicyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PolicyIdentifierPolicyType:
    return from_query_text(el.text or "")
