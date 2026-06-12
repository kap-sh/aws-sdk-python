"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the units for GOP size. If you don't specify a value here, by default the encoder measures GOP size in frames."""
Mpeg2GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FRAMES",
        "SECONDS",
    )
)


def serialize_json(value: Mpeg2GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2GopSizeUnits:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2GopSizeUnits value: {data!r}")
    return cast(Mpeg2GopSizeUnits, data)
