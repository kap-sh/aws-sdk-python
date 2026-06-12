"""Generated from Smithy shape ``com.amazonaws.ses#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

EventType: TypeAlias = Literal[
    "send",
    "reject",
    "bounce",
    "complaint",
    "delivery",
    "open",
    "click",
    "renderingFailure",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "send",
        "reject",
        "bounce",
        "complaint",
        "delivery",
        "open",
        "click",
        "renderingFailure",
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
