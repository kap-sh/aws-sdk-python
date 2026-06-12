"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackRefactorStatus: TypeAlias = Literal[
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_COMPLETE",
    "DELETE_FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_IN_PROGRESS",
        "CREATE_COMPLETE",
        "CREATE_FAILED",
        "DELETE_IN_PROGRESS",
        "DELETE_COMPLETE",
        "DELETE_FAILED",
    )
)


def to_query_text(value: StackRefactorStatus) -> str:
    return value


def from_query_text(text: str) -> StackRefactorStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StackRefactorStatus value: {text!r}")
    return cast(StackRefactorStatus, text)


def serialize_query(
    value: StackRefactorStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackRefactorStatus:
    return from_query_text(el.text or "")
