"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3AtmosBitstreamMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the bitstream mode for the E-AC-3 stream that the encoder emits. For more information about the EAC3 bitstream mode, see ATSC A/52-2012 (Annex E)."""
Eac3AtmosBitstreamMode: TypeAlias = Literal["COMPLETE_MAIN",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("COMPLETE_MAIN",))


def serialize_json(value: Eac3AtmosBitstreamMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3AtmosBitstreamMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Eac3AtmosBitstreamMode value: {data!r}")
    return cast(Eac3AtmosBitstreamMode, data)
