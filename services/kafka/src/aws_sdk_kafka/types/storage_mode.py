"""Generated from Smithy shape ``com.amazonaws.kafka#StorageMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kafka.errors import DeserializationError

"""Controls storage mode for various supported storage tiers."""
StorageMode: TypeAlias = Literal[
    "LOCAL",
    "TIERED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOCAL",
        "TIERED",
    )
)


def serialize_json(value: StorageMode) -> str:
    return value


def deserialize_json(data: str) -> StorageMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageMode value: {data!r}")
    return cast(StorageMode, data)
