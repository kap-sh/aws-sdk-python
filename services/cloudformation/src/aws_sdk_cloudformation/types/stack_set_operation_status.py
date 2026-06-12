"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackSetOperationStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "STOPPING",
    "STOPPED",
    "QUEUED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "STOPPING",
        "STOPPED",
        "QUEUED",
    )
)


def to_query_text(value: StackSetOperationStatus) -> str:
    return value


def from_query_text(text: str) -> StackSetOperationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StackSetOperationStatus value: {text!r}")
    return cast(StackSetOperationStatus, text)


def serialize_query(
    value: StackSetOperationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackSetOperationStatus:
    return from_query_text(el.text or "")
