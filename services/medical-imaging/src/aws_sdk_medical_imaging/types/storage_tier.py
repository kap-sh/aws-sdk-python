"""Generated from Smithy shape ``com.amazonaws.medicalimaging#StorageTier``."""

from typing import Literal, TypeAlias, cast

"""Storage tier for image sets"""
StorageTier: TypeAlias = Literal[
    "FREQUENT_ACCESS",
    "ARCHIVE_INSTANT_ACCESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageTier) -> str:
    return value


def deserialize_json(data: str) -> StorageTier:
    return cast(StorageTier, data)
