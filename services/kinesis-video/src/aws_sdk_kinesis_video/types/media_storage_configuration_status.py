"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#MediaStorageConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

MediaStorageConfigurationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaStorageConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> MediaStorageConfigurationStatus:
    return cast(MediaStorageConfigurationStatus, data)
