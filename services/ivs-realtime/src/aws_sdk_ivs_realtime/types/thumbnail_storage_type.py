"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ThumbnailStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

ThumbnailStorageType: TypeAlias = Literal[
    "SEQUENTIAL",
    "LATEST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SEQUENTIAL",
        "LATEST",
    )
)


def serialize_json(value: ThumbnailStorageType) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailStorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThumbnailStorageType value: {data!r}")
    return cast(ThumbnailStorageType, data)
