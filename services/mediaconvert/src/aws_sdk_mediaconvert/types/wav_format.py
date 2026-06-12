"""Generated from Smithy shape ``com.amazonaws.mediaconvert#WavFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the file format for your wave audio output. To use a RIFF wave format: Keep the default value, RIFF. If your output audio is likely to exceed 4GB in file size, or if you otherwise need the extended support of the RF64 format: Choose RF64. If your player only supports the extensible wave format: Choose Extensible."""
WavFormat: TypeAlias = Literal[
    "RIFF",
    "RF64",
    "EXTENSIBLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RIFF",
        "RF64",
        "EXTENSIBLE",
    )
)


def serialize_json(value: WavFormat) -> str:
    return value


def deserialize_json(data: str) -> WavFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WavFormat value: {data!r}")
    return cast(WavFormat, data)
