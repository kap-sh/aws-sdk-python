"""Generated from Smithy shape ``com.amazonaws.mediastoredata#UploadAvailability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediastore_data.errors import DeserializationError

UploadAvailability: TypeAlias = Literal[
    "STANDARD",
    "STREAMING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "STREAMING",
    )
)


def serialize_json(value: UploadAvailability) -> str:
    return value


def deserialize_json(data: str) -> UploadAvailability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UploadAvailability value: {data!r}")
    return cast(UploadAvailability, data)
