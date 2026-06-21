"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#PresetSpeke20Video``."""

from typing import Literal, TypeAlias, cast

PresetSpeke20Video: TypeAlias = Literal[
    "PRESET-VIDEO-1",
    "PRESET-VIDEO-2",
    "PRESET-VIDEO-3",
    "PRESET-VIDEO-4",
    "PRESET-VIDEO-5",
    "PRESET-VIDEO-6",
    "PRESET-VIDEO-7",
    "PRESET-VIDEO-8",
    "SHARED",
    "UNENCRYPTED",
]


# --- restJson1 ser/de ---
def serialize_json(value: PresetSpeke20Video) -> str:
    return value


def deserialize_json(data: str) -> PresetSpeke20Video:
    return cast(PresetSpeke20Video, data)
