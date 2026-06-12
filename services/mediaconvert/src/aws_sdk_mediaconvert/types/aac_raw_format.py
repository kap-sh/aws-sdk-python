"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacRawFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose \"No container\" for the output container."""
AacRawFormat: TypeAlias = Literal[
    "LATM_LOAS",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATM_LOAS",
        "NONE",
    )
)


def serialize_json(value: AacRawFormat) -> str:
    return value


def deserialize_json(data: str) -> AacRawFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AacRawFormat value: {data!r}")
    return cast(AacRawFormat, data)
