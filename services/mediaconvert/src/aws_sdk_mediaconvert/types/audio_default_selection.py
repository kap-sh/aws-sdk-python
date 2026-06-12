"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioDefaultSelection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify a fallback audio selector for this input. Use to ensure outputs have audio even when the audio selector you specify in your output is missing from the source. DEFAULT (Checked in the MediaConvert console): If your output settings specify an audio selector that does not exist in this input, MediaConvert uses this audio selector instead. This is useful when you have multiple inputs with a different number of audio tracks. NOT_DEFAULT (Unchecked in the MediaConvert console): MediaConvert will not fallback from any missing audio selector. Any output specifying a missing audio selector will be silent."""
AudioDefaultSelection: TypeAlias = Literal[
    "DEFAULT",
    "NOT_DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "NOT_DEFAULT",
    )
)


def serialize_json(value: AudioDefaultSelection) -> str:
    return value


def deserialize_json(data: str) -> AudioDefaultSelection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AudioDefaultSelection value: {data!r}")
    return cast(AudioDefaultSelection, data)
