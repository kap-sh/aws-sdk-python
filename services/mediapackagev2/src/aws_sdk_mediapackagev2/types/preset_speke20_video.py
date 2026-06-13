"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#PresetSpeke20Video``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

PresetSpeke20Video: TypeAlias = Literal[
    "PRESET_VIDEO_1",
    "PRESET_VIDEO_2",
    "PRESET_VIDEO_3",
    "PRESET_VIDEO_4",
    "PRESET_VIDEO_5",
    "PRESET_VIDEO_6",
    "PRESET_VIDEO_7",
    "PRESET_VIDEO_8",
    "SHARED",
    "UNENCRYPTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRESET_VIDEO_1",
        "PRESET_VIDEO_2",
        "PRESET_VIDEO_3",
        "PRESET_VIDEO_4",
        "PRESET_VIDEO_5",
        "PRESET_VIDEO_6",
        "PRESET_VIDEO_7",
        "PRESET_VIDEO_8",
        "SHARED",
        "UNENCRYPTED",
    )
)


def serialize_json(value: PresetSpeke20Video) -> str:
    return value


def deserialize_json(data: str) -> PresetSpeke20Video:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PresetSpeke20Video value: {data!r}")
    return cast(PresetSpeke20Video, data)
