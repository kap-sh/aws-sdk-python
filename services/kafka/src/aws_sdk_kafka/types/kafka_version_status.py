"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaVersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

KafkaVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DEPRECATED",
    )
)


def serialize_json(value: KafkaVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> KafkaVersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KafkaVersionStatus value: {data!r}")
    return cast(KafkaVersionStatus, data)
