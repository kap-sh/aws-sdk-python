"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingMetric``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

EventSourceMappingMetric: TypeAlias = Literal[
    "EventCount",
    "ErrorCount",
    "KafkaMetrics",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EventCount",
        "ErrorCount",
        "KafkaMetrics",
    )
)


def serialize_json(value: EventSourceMappingMetric) -> str:
    return value


def deserialize_json(data: str) -> EventSourceMappingMetric:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventSourceMappingMetric value: {data!r}")
    return cast(EventSourceMappingMetric, data)
