"""Generated from Smithy shape ``com.amazonaws.mediaconvert#UncompressedInterlaceMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. Choose the scan line type for this output. If you don't specify a value, MediaConvert will create a progressive output."""
UncompressedInterlaceMode: TypeAlias = Literal[
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


def serialize_json(value: UncompressedInterlaceMode) -> str:
    return value


def deserialize_json(data: str) -> UncompressedInterlaceMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UncompressedInterlaceMode value: {data!r}")
    return cast(UncompressedInterlaceMode, data)
