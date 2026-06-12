"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackRefactorExecutionStatus: TypeAlias = Literal[
    "UNAVAILABLE",
    "AVAILABLE",
    "OBSOLETE",
    "EXECUTE_IN_PROGRESS",
    "EXECUTE_COMPLETE",
    "EXECUTE_FAILED",
    "ROLLBACK_IN_PROGRESS",
    "ROLLBACK_COMPLETE",
    "ROLLBACK_FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNAVAILABLE",
        "AVAILABLE",
        "OBSOLETE",
        "EXECUTE_IN_PROGRESS",
        "EXECUTE_COMPLETE",
        "EXECUTE_FAILED",
        "ROLLBACK_IN_PROGRESS",
        "ROLLBACK_COMPLETE",
        "ROLLBACK_FAILED",
    )
)


def to_query_text(value: StackRefactorExecutionStatus) -> str:
    return value


def from_query_text(text: str) -> StackRefactorExecutionStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown StackRefactorExecutionStatus value: {text!r}"
        )
    return cast(StackRefactorExecutionStatus, text)


def serialize_query(
    value: StackRefactorExecutionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackRefactorExecutionStatus:
    return from_query_text(el.text or "")
