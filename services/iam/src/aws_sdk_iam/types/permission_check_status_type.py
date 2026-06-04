"""Generated from Smithy shape ``com.amazonaws.iam#permissionCheckStatusType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

permissionCheckStatusType: TypeAlias = Literal[
    "COMPLETE",
    "IN_PROGRESS",
    "FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETE",
        "IN_PROGRESS",
        "FAILED",
    )
)


def to_query_text(value: permissionCheckStatusType) -> str:
    return value


def from_query_text(text: str) -> permissionCheckStatusType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown permissionCheckStatusType value: {text!r}")
    return cast(permissionCheckStatusType, text)


def serialize_query(
    value: permissionCheckStatusType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> permissionCheckStatusType:
    return from_query_text(el.text or "")
