"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#PresetSpeke20Audio``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackage_vod.errors import DeserializationError

PresetSpeke20Audio: TypeAlias = Literal[
    "PRESET-AUDIO-1",
    "PRESET-AUDIO-2",
    "PRESET-AUDIO-3",
    "SHARED",
    "UNENCRYPTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRESET-AUDIO-1",
        "PRESET-AUDIO-2",
        "PRESET-AUDIO-3",
        "SHARED",
        "UNENCRYPTED",
    )
)


def serialize_json(value: PresetSpeke20Audio) -> str:
    return value


def deserialize_json(data: str) -> PresetSpeke20Audio:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PresetSpeke20Audio value: {data!r}")
    return cast(PresetSpeke20Audio, data)
