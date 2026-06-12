"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricStreamOutputFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

MetricStreamOutputFormat: TypeAlias = Literal[
    "json",
    "opentelemetry0.7",
    "opentelemetry1.0",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "json",
        "opentelemetry0.7",
        "opentelemetry1.0",
    )
)


def serialize_aws_json_1_0(value: MetricStreamOutputFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MetricStreamOutputFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MetricStreamOutputFormat value: {data!r}")
    return cast(MetricStreamOutputFormat, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "json",
        "opentelemetry0.7",
        "opentelemetry1.0",
    )
)


def to_query_text(value: MetricStreamOutputFormat) -> str:
    return value


def from_query_text(text: str) -> MetricStreamOutputFormat:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MetricStreamOutputFormat value: {text!r}")
    return cast(MetricStreamOutputFormat, text)


def serialize_query(
    value: MetricStreamOutputFormat, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MetricStreamOutputFormat:
    return from_query_text(el.text or "")
