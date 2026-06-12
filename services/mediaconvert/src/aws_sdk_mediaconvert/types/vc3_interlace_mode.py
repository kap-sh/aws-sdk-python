"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vc3InterlaceMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output."""
Vc3InterlaceMode: TypeAlias = Literal[
    "INTERLACED",
    "PROGRESSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERLACED",
        "PROGRESSIVE",
    )
)


def serialize_json(value: Vc3InterlaceMode) -> str:
    return value


def deserialize_json(data: str) -> Vc3InterlaceMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Vc3InterlaceMode value: {data!r}")
    return cast(Vc3InterlaceMode, data)
