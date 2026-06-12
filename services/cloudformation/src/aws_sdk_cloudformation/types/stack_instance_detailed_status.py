"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceDetailedStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackInstanceDetailedStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLED",
    "INOPERABLE",
    "SKIPPED_SUSPENDED_ACCOUNT",
    "FAILED_IMPORT",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
        "INOPERABLE",
        "SKIPPED_SUSPENDED_ACCOUNT",
        "FAILED_IMPORT",
    )
)


def to_query_text(value: StackInstanceDetailedStatus) -> str:
    return value


def from_query_text(text: str) -> StackInstanceDetailedStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown StackInstanceDetailedStatus value: {text!r}"
        )
    return cast(StackInstanceDetailedStatus, text)


def serialize_query(
    value: StackInstanceDetailedStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackInstanceDetailedStatus:
    return from_query_text(el.text or "")
