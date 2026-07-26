"""Generated from Smithy shape ``com.amazonaws.iotsitewise#StorageType``."""

from typing import Literal, TypeAlias, cast

StorageType: TypeAlias = Literal[
    "SITEWISE_DEFAULT_STORAGE",
    "MULTI_LAYER_STORAGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageType) -> str:
    return value


def deserialize_json(data: str) -> StorageType:
    return cast(StorageType, data)
