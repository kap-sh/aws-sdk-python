"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AudioChannelTag``."""

from typing import Literal, TypeAlias, cast

"""Specify the QuickTime audio channel layout tags for the audio channels in this audio track. Enter channel layout tags in the same order as your output's audio channel order. For example, if your output audio track has a left and a right channel, enter Left (L) for the first channel and Right (R) for the second. If your output has multiple single-channel audio tracks, enter a single channel layout tag for each track."""
AudioChannelTag: TypeAlias = Literal[
    "L",
    "R",
    "C",
    "LFE",
    "LS",
    "RS",
    "LC",
    "RC",
    "CS",
    "LSD",
    "RSD",
    "TCS",
    "VHL",
    "VHC",
    "VHR",
    "TBL",
    "TBC",
    "TBR",
    "RSL",
    "RSR",
    "LW",
    "RW",
    "LFE2",
    "LT",
    "RT",
    "HI",
    "NAR",
    "M",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudioChannelTag) -> str:
    return value


def deserialize_json(data: str) -> AudioChannelTag:
    return cast(AudioChannelTag, data)
