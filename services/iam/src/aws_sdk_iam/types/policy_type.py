"""Generated from Smithy shape ``com.amazonaws.iam#policyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

policyType: TypeAlias = Literal[
    "INLINE",
    "MANAGED",
]


# --- awsQuery ser/de ---
def to_query_text(value: policyType) -> str:
    return value


def from_query_text(text: str) -> policyType:
    return cast(policyType, text)


def serialize_query(
    value: policyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> policyType:
    return from_query_text(el.text or "")
