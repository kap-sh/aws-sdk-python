"""Generated from Smithy shape ``com.amazonaws.iam#PolicySourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

PolicySourceType: TypeAlias = Literal[
    "user",
    "group",
    "role",
    "aws-managed",
    "user-managed",
    "resource",
    "none",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "user",
        "group",
        "role",
        "aws-managed",
        "user-managed",
        "resource",
        "none",
    )
)


def to_query_text(value: PolicySourceType) -> str:
    return value


def from_query_text(text: str) -> PolicySourceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PolicySourceType value: {text!r}")
    return cast(PolicySourceType, text)


def serialize_query(
    value: PolicySourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PolicySourceType:
    return from_query_text(el.text or "")
