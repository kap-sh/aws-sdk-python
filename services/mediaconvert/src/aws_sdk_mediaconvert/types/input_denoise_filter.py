"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputDenoiseFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enable Denoise to filter noise from the input. Default is disabled. Only applicable to MPEG2, H.264, H.265, and uncompressed video inputs."""
InputDenoiseFilter: TypeAlias = Literal[
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


def serialize_json(value: InputDenoiseFilter) -> str:
    return value


def deserialize_json(data: str) -> InputDenoiseFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDenoiseFilter value: {data!r}")
    return cast(InputDenoiseFilter, data)
