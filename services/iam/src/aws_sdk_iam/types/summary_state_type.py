"""Generated from Smithy shape ``com.amazonaws.iam#summaryStateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

summaryStateType: TypeAlias = Literal[
    "AVAILABLE",
    "NOT_AVAILABLE",
    "NOT_SUPPORTED",
    "FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "NOT_AVAILABLE",
        "NOT_SUPPORTED",
        "FAILED",
    )
)


def to_query_text(value: summaryStateType) -> str:
    return value


def from_query_text(text: str) -> summaryStateType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown summaryStateType value: {text!r}")
    return cast(summaryStateType, text)


def serialize_query(
    value: summaryStateType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> summaryStateType:
    return from_query_text(el.text or "")
