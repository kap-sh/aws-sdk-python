"""Generated from Smithy shape ``com.amazonaws.cloudwatch#ScanBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

ScanBy: TypeAlias = Literal[
    "TimestampDescending",
    "TimestampAscending",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TimestampDescending",
        "TimestampAscending",
    )
)


def serialize_aws_json_1_0(value: ScanBy) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScanBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScanBy value: {data!r}")
    return cast(ScanBy, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TimestampDescending",
        "TimestampAscending",
    )
)


def to_query_text(value: ScanBy) -> str:
    return value


def from_query_text(text: str) -> ScanBy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ScanBy value: {text!r}")
    return cast(ScanBy, text)


def serialize_query(value: ScanBy, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ScanBy:
    return from_query_text(el.text or "")
