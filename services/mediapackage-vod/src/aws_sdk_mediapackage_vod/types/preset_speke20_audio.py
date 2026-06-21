"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#PresetSpeke20Audio``."""

from typing import Literal, TypeAlias, cast

PresetSpeke20Audio: TypeAlias = Literal[
    "PRESET-AUDIO-1",
    "PRESET-AUDIO-2",
    "PRESET-AUDIO-3",
    "SHARED",
    "UNENCRYPTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PresetSpeke20Audio) -> str:
    return value


def deserialize_json(data: str) -> PresetSpeke20Audio:
    return cast(PresetSpeke20Audio, data)
