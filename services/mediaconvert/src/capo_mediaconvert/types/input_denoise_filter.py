"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputDenoiseFilter``."""

from typing import Literal, TypeAlias, cast

"""Enable Denoise to filter noise from the input. Default is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs."""
InputDenoiseFilter: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDenoiseFilter) -> str:
    return value


def deserialize_json(data: str) -> InputDenoiseFilter:
    return cast(InputDenoiseFilter, data)
