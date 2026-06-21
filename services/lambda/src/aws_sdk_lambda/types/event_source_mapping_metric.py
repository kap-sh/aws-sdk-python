"""Generated from Smithy shape ``com.amazonaws.lambda#EventSourceMappingMetric``."""

from typing import Literal, TypeAlias, cast

EventSourceMappingMetric: TypeAlias = Literal[
    "EventCount",
    "ErrorCount",
    "KafkaMetrics",
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSourceMappingMetric) -> str:
    return value


def deserialize_json(data: str) -> EventSourceMappingMetric:
    return cast(EventSourceMappingMetric, data)
