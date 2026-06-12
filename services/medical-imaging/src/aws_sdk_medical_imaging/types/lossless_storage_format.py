"""Generated from Smithy shape ``com.amazonaws.medicalimaging#LosslessStorageFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medical_imaging.errors import DeserializationError

LosslessStorageFormat: TypeAlias = Literal[
    "HTJ2K",
    "JPEG_2000_LOSSLESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTJ2K",
        "JPEG_2000_LOSSLESS",
    )
)


def serialize_json(value: LosslessStorageFormat) -> str:
    return value


def deserialize_json(data: str) -> LosslessStorageFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LosslessStorageFormat value: {data!r}")
    return cast(LosslessStorageFormat, data)
