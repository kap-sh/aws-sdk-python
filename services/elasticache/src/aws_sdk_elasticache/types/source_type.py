"""Generated from Smithy shape ``com.amazonaws.elasticache#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "cache-cluster",
    "cache-parameter-group",
    "cache-security-group",
    "cache-subnet-group",
    "replication-group",
    "serverless-cache",
    "serverless-cache-snapshot",
    "user",
    "user-group",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "cache-cluster",
        "cache-parameter-group",
        "cache-security-group",
        "cache-subnet-group",
        "replication-group",
        "serverless-cache",
        "serverless-cache-snapshot",
        "user",
        "user-group",
    )
)


def to_query_text(value: SourceType) -> str:
    return value


def from_query_text(text: str) -> SourceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {text!r}")
    return cast(SourceType, text)


def serialize_query(
    value: SourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SourceType:
    return from_query_text(el.text or "")
