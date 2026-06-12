"""Generated from Smithy shape ``com.amazonaws.kafka#ConsumerGroupOffsetSyncMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""<p>The consumer group offset synchronization mode. With LEGACY, offsets are synchronized when producers write to the source cluster. With ENHANCED, consumer offsets are synchronized regardless of producer location. ENHANCED requires a corresponding replicator that replicates data from the target cluster to the source cluster.</p>"""
ConsumerGroupOffsetSyncMode: TypeAlias = Literal[
    "LEGACY",
    "ENHANCED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LEGACY",
        "ENHANCED",
    )
)


def serialize_json(value: ConsumerGroupOffsetSyncMode) -> str:
    return value


def deserialize_json(data: str) -> ConsumerGroupOffsetSyncMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConsumerGroupOffsetSyncMode value: {data!r}"
        )
    return cast(ConsumerGroupOffsetSyncMode, data)
