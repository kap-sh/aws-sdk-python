"""Generated from Smithy shape ``com.amazonaws.cloudformation#ExecutionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ExecutionStatus: TypeAlias = Literal[
    "UNAVAILABLE",
    "AVAILABLE",
    "EXECUTE_IN_PROGRESS",
    "EXECUTE_COMPLETE",
    "EXECUTE_FAILED",
    "OBSOLETE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNAVAILABLE",
        "AVAILABLE",
        "EXECUTE_IN_PROGRESS",
        "EXECUTE_COMPLETE",
        "EXECUTE_FAILED",
        "OBSOLETE",
    )
)


def to_query_text(value: ExecutionStatus) -> str:
    return value


def from_query_text(text: str) -> ExecutionStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatus value: {text!r}")
    return cast(ExecutionStatus, text)


def serialize_query(
    value: ExecutionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ExecutionStatus:
    return from_query_text(el.text or "")
