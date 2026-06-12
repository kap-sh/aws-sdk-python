"""Generated from Smithy shape ``com.amazonaws.mediaconvert#PresetSpeke20Video``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify which SPEKE version 2.0 video preset MediaConvert uses to request content keys from your SPEKE server. For more information, see: https://docs.aws.amazon.com/mediaconvert/latest/ug/drm-content-speke-v2-presets.html To encrypt to your video outputs, choose from the following: Video preset 1, Video preset 2, Video preset 3, Video preset 4, Video preset 5, Video preset 6, Video preset 7, or Video preset 8. To encrypt your video outputs, using the same content key for both your video and audio outputs: Choose Shared. When you do, you must also set SPEKE v2.0 audio preset to Shared. To not encrypt your video outputs: Choose Unencrypted. When you do, to encrypt your audio outputs, you must also specify a SPEKE v2.0 audio preset (other than Shared or Unencrypted)."""
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
