"""Generated from Smithy shape ``com.amazonaws.cloudformation#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

EventType: TypeAlias = Literal[
    "STACK_EVENT",
    "PROGRESS_EVENT",
    "VALIDATION_ERROR",
    "PROVISIONING_ERROR",
    "HOOK_INVOCATION_ERROR",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STACK_EVENT",
        "PROGRESS_EVENT",
        "VALIDATION_ERROR",
        "PROVISIONING_ERROR",
        "HOOK_INVOCATION_ERROR",
    )
)


def to_query_text(value: EventType) -> str:
    return value


def from_query_text(text: str) -> EventType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {text!r}")
    return cast(EventType, text)


def serialize_query(
    value: EventType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EventType:
    return from_query_text(el.text or "")
