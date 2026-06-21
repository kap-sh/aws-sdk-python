"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EventSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element

EventSeverity: TypeAlias = Literal[
    "TRACE",
    "DEBUG",
    "INFO",
    "WARN",
    "ERROR",
    "FATAL",
]


# --- awsQuery ser/de ---
def to_query_text(value: EventSeverity) -> str:
    return value


def from_query_text(text: str) -> EventSeverity:
    return cast(EventSeverity, text)


def serialize_query(
    value: EventSeverity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EventSeverity:
    return from_query_text(el.text or "")
