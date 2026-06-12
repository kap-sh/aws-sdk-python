"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ThumbnailRecordingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ivs_realtime.errors import DeserializationError

ThumbnailRecordingMode: TypeAlias = Literal[
    "INTERVAL",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERVAL",
        "DISABLED",
    )
)


def serialize_json(value: ThumbnailRecordingMode) -> str:
    return value


def deserialize_json(data: str) -> ThumbnailRecordingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ThumbnailRecordingMode value: {data!r}")
    return cast(ThumbnailRecordingMode, data)
