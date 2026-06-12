"""Generated from Smithy shape ``com.amazonaws.redshift#LogDestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

LogDestinationType: TypeAlias = Literal[
    "s3",
    "cloudwatch",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "s3",
        "cloudwatch",
    )
)


def to_query_text(value: LogDestinationType) -> str:
    return value


def from_query_text(text: str) -> LogDestinationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LogDestinationType value: {text!r}")
    return cast(LogDestinationType, text)


def serialize_query(
    value: LogDestinationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LogDestinationType:
    return from_query_text(el.text or "")
