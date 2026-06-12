"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#EventPublishers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.event_publisher

EventPublishers: TypeAlias = list[
    "aws_sdk_codeguruprofiler.types.event_publisher.EventPublisher"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventPublishers) -> list:
    return list(value)


def deserialize_json(data: list) -> EventPublishers:
    return list(data)
