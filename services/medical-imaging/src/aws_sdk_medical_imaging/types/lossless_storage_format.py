"""Generated from Smithy shape ``com.amazonaws.medicalimaging#LosslessStorageFormat``."""

from typing import Literal, TypeAlias, cast

LosslessStorageFormat: TypeAlias = Literal[
    "HTJ2K",
    "JPEG_2000_LOSSLESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: LosslessStorageFormat) -> str:
    return value


def deserialize_json(data: str) -> LosslessStorageFormat:
    return cast(LosslessStorageFormat, data)
