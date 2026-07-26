"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#PresetSpeke20Audio``."""

from typing import Literal, TypeAlias, cast

PresetSpeke20Audio: TypeAlias = Literal[
    "PRESET_AUDIO_1",
    "PRESET_AUDIO_2",
    "PRESET_AUDIO_3",
    "SHARED",
    "UNENCRYPTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PresetSpeke20Audio) -> str:
    return value


def deserialize_json(data: str) -> PresetSpeke20Audio:
    return cast(PresetSpeke20Audio, data)
