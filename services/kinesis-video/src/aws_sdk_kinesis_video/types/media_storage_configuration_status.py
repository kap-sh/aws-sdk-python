"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MediaStorageConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video.errors import DeserializationError

MediaStorageConfigurationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: MediaStorageConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> MediaStorageConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MediaStorageConfigurationStatus value: {data!r}"
        )
    return cast(MediaStorageConfigurationStatus, data)
