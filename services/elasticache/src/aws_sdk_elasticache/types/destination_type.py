"""Generated from Smithy shape ``com.amazonaws.elasticache#DestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

DestinationType: TypeAlias = Literal[
    "cloudwatch-logs",
    "kinesis-firehose",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cloudwatch-logs",
        "kinesis-firehose",
    )
)


def to_query_text(value: DestinationType) -> str:
    return value


def from_query_text(text: str) -> DestinationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DestinationType value: {text!r}")
    return cast(DestinationType, text)


def serialize_query(
    value: DestinationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DestinationType:
    return from_query_text(el.text or "")
