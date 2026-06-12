"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackInstanceFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackInstanceFilterName: TypeAlias = Literal[
    "DETAILED_STATUS",
    "LAST_OPERATION_ID",
    "DRIFT_STATUS",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DETAILED_STATUS",
        "LAST_OPERATION_ID",
        "DRIFT_STATUS",
    )
)


def to_query_text(value: StackInstanceFilterName) -> str:
    return value


def from_query_text(text: str) -> StackInstanceFilterName:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StackInstanceFilterName value: {text!r}")
    return cast(StackInstanceFilterName, text)


def serialize_query(
    value: StackInstanceFilterName, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackInstanceFilterName:
    return from_query_text(el.text or "")
