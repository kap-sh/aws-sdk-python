"""Generated from Smithy shape ``com.amazonaws.medicalimaging#StorageTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medical_imaging.errors import DeserializationError

"""Storage tier for image sets"""
StorageTier: TypeAlias = Literal[
    "FREQUENT_ACCESS",
    "ARCHIVE_INSTANT_ACCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FREQUENT_ACCESS",
        "ARCHIVE_INSTANT_ACCESS",
    )
)


def serialize_json(value: StorageTier) -> str:
    return value


def deserialize_json(data: str) -> StorageTier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageTier value: {data!r}")
    return cast(StorageTier, data)
