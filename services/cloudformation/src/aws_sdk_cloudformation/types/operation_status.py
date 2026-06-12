"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

OperationStatus: TypeAlias = Literal[
    "PENDING",
    "IN_PROGRESS",
    "SUCCESS",
    "FAILED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "IN_PROGRESS",
        "SUCCESS",
        "FAILED",
    )
)


def to_query_text(value: OperationStatus) -> str:
    return value


def from_query_text(text: str) -> OperationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OperationStatus value: {text!r}")
    return cast(OperationStatus, text)


def serialize_query(
    value: OperationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OperationStatus:
    return from_query_text(el.text or "")
