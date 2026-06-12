"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MsSmoothFragmentLengthControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify how you want MediaConvert to determine the fragment length. Choose Exact to have the encoder use the exact length that you specify with the setting Fragment length. This might result in extra I-frames. Choose Multiple of GOP to have the encoder round up the segment lengths to match the next GOP boundary."""
MsSmoothFragmentLengthControl: TypeAlias = Literal[
    "EXACT",
    "GOP_MULTIPLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EXACT",
        "GOP_MULTIPLE",
    )
)


def serialize_json(value: MsSmoothFragmentLengthControl) -> str:
    return value


def deserialize_json(data: str) -> MsSmoothFragmentLengthControl:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown MsSmoothFragmentLengthControl value: {data!r}"
        )
    return cast(MsSmoothFragmentLengthControl, data)
