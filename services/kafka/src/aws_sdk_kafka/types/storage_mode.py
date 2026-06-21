"""Generated from Smithy shape ``com.amazonaws.kafka#StorageMode``."""

from typing import Literal, TypeAlias, cast

"""Controls storage mode for various supported storage tiers."""
StorageMode: TypeAlias = Literal[
    "LOCAL",
    "TIERED",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageMode) -> str:
    return value


def deserialize_json(data: str) -> StorageMode:
    return cast(StorageMode, data)
