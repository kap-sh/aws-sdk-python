"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationResultStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackSetOperationResultStatus: TypeAlias = Literal[
    "PENDING",
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "RUNNING",
        "SUCCEEDED",
        "FAILED",
        "CANCELLED",
    )
)


def to_query_text(value: StackSetOperationResultStatus) -> str:
    return value


def from_query_text(text: str) -> StackSetOperationResultStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown StackSetOperationResultStatus value: {text!r}"
        )
    return cast(StackSetOperationResultStatus, text)


def serialize_query(
    value: StackSetOperationResultStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackSetOperationResultStatus:
    return from_query_text(el.text or "")
