"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EventSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

EventSeverity: TypeAlias = Literal[
    "TRACE",
    "DEBUG",
    "INFO",
    "WARN",
    "ERROR",
    "FATAL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRACE",
        "DEBUG",
        "INFO",
        "WARN",
        "ERROR",
        "FATAL",
    )
)


def to_query_text(value: EventSeverity) -> str:
    return value


def from_query_text(text: str) -> EventSeverity:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EventSeverity value: {text!r}")
    return cast(EventSeverity, text)


def serialize_query(
    value: EventSeverity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EventSeverity:
    return from_query_text(el.text or "")
