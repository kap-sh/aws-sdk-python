"""Generated from Smithy shape ``com.amazonaws.iam#sortKeyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

sortKeyType: TypeAlias = Literal[
    "SERVICE_NAMESPACE_ASCENDING",
    "SERVICE_NAMESPACE_DESCENDING",
    "LAST_AUTHENTICATED_TIME_ASCENDING",
    "LAST_AUTHENTICATED_TIME_DESCENDING",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_NAMESPACE_ASCENDING",
        "SERVICE_NAMESPACE_DESCENDING",
        "LAST_AUTHENTICATED_TIME_ASCENDING",
        "LAST_AUTHENTICATED_TIME_DESCENDING",
    )
)


def to_query_text(value: sortKeyType) -> str:
    return value


def from_query_text(text: str) -> sortKeyType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown sortKeyType value: {text!r}")
    return cast(sortKeyType, text)


def serialize_query(
    value: sortKeyType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> sortKeyType:
    return from_query_text(el.text or "")
