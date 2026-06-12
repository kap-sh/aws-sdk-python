"""Generated from Smithy shape ``com.amazonaws.iotsitewise#StorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

StorageType: TypeAlias = Literal[
    "SITEWISE_DEFAULT_STORAGE",
    "MULTI_LAYER_STORAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SITEWISE_DEFAULT_STORAGE",
        "MULTI_LAYER_STORAGE",
    )
)


def serialize_json(value: StorageType) -> str:
    return value


def deserialize_json(data: str) -> StorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageType value: {data!r}")
    return cast(StorageType, data)
