"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DynamicAudioSelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify which audio tracks to dynamically select from your source. To select all audio tracks: Keep the default value, All tracks. To select all audio tracks with a specific language code: Choose Language code. When you do, you must also specify a language code under the Language code setting. If there is no matching Language code in your source, then no track will be selected."""
DynamicAudioSelectorType: TypeAlias = Literal[
    "ALL_TRACKS",
    "LANGUAGE_CODE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL_TRACKS",
        "LANGUAGE_CODE",
    )
)


def serialize_json(value: DynamicAudioSelectorType) -> str:
    return value


def deserialize_json(data: str) -> DynamicAudioSelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DynamicAudioSelectorType value: {data!r}")
    return cast(DynamicAudioSelectorType, data)
