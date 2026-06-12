"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AlphaBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Ignore this setting unless this input is a QuickTime animation with an alpha channel. Use this setting to create separate Key and Fill outputs. In each output, specify which part of the input MediaConvert uses. Leave this setting at the default value DISCARD to delete the alpha channel and preserve the video. Set it to REMAP_TO_LUMA to delete the video and map the alpha channel to the luma channel of your outputs."""
AlphaBehavior: TypeAlias = Literal[
    "DISCARD",
    "REMAP_TO_LUMA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISCARD",
        "REMAP_TO_LUMA",
    )
)


def serialize_json(value: AlphaBehavior) -> str:
    return value


def deserialize_json(data: str) -> AlphaBehavior:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlphaBehavior value: {data!r}")
    return cast(AlphaBehavior, data)
