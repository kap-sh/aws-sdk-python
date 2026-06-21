"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputDeblockFilter``."""

from typing import Literal, TypeAlias, cast

"""Enable Deblock to produce smoother motion in the output. Default is disabled. Only manually controllable for MPEG2 and uncompressed video inputs."""
InputDeblockFilter: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeblockFilter) -> str:
    return value


def deserialize_json(data: str) -> InputDeblockFilter:
    return cast(InputDeblockFilter, data)
