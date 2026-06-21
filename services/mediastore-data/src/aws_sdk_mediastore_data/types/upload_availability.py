"""Generated from Smithy shape ``com.amazonaws.mediastoredata#UploadAvailability``."""

from typing import Literal, TypeAlias, cast

UploadAvailability: TypeAlias = Literal[
    "STANDARD",
    "STREAMING",
]


# --- restJson1 ser/de ---
def serialize_json(value: UploadAvailability) -> str:
    return value


def deserialize_json(data: str) -> UploadAvailability:
    return cast(UploadAvailability, data)
