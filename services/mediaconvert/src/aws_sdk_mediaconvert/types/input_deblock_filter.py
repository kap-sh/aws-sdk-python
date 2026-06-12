"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputDeblockFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enable Deblock to produce smoother motion in the output. Default is disabled. Only manually controllable for MPEG2 and uncompressed video inputs."""
InputDeblockFilter: TypeAlias = Literal[
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


def serialize_json(value: InputDeblockFilter) -> str:
    return value


def deserialize_json(data: str) -> InputDeblockFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeblockFilter value: {data!r}")
    return cast(InputDeblockFilter, data)
