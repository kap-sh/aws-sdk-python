"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaVersionStatus``."""

from typing import Literal, TypeAlias, cast

KafkaVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: KafkaVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> KafkaVersionStatus:
    return cast(KafkaVersionStatus, data)
