"""Generated from Smithy shape ``com.amazonaws.kafka#ConsumerGroupOffsetSyncMode``."""

from typing import Literal, TypeAlias, cast

"""<p>The consumer group offset synchronization mode. With LEGACY, offsets are synchronized when producers write to the source cluster. With ENHANCED, consumer offsets are synchronized regardless of producer location. ENHANCED requires a corresponding replicator that replicates data from the target cluster to the source cluster.</p>"""
ConsumerGroupOffsetSyncMode: TypeAlias = Literal[
    "LEGACY",
    "ENHANCED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsumerGroupOffsetSyncMode) -> str:
    return value


def deserialize_json(data: str) -> ConsumerGroupOffsetSyncMode:
    return cast(ConsumerGroupOffsetSyncMode, data)
