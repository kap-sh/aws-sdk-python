"""Generated from Smithy shape ``com.amazonaws.elasticache#LogFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

LogFormat: TypeAlias = Literal[
    "text",
    "json",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "text",
        "json",
    )
)


def to_query_text(value: LogFormat) -> str:
    return value


def from_query_text(text: str) -> LogFormat:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LogFormat value: {text!r}")
    return cast(LogFormat, text)


def serialize_query(
    value: LogFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LogFormat:
    return from_query_text(el.text or "")
