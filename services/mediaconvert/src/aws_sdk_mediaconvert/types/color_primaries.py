"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ColorPrimaries``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""The color space primaries of the video track, defining the red, green, and blue color coordinates used for the video. This information helps ensure accurate color reproduction during playback and transcoding."""
ColorPrimaries: TypeAlias = Literal[
    "ITU_709",
    "UNSPECIFIED",
    "RESERVED",
    "ITU_470M",
    "ITU_470BG",
    "SMPTE_170M",
    "SMPTE_240M",
    "GENERIC_FILM",
    "ITU_2020",
    "SMPTE_428_1",
    "SMPTE_431_2",
    "SMPTE_EG_432_1",
    "IPT",
    "SMPTE_2067XYZ",
    "EBU_3213_E",
    "LAST",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ITU_709",
        "UNSPECIFIED",
        "RESERVED",
        "ITU_470M",
        "ITU_470BG",
        "SMPTE_170M",
        "SMPTE_240M",
        "GENERIC_FILM",
        "ITU_2020",
        "SMPTE_428_1",
        "SMPTE_431_2",
        "SMPTE_EG_432_1",
        "IPT",
        "SMPTE_2067XYZ",
        "EBU_3213_E",
        "LAST",
    )
)


def serialize_json(value: ColorPrimaries) -> str:
    return value


def deserialize_json(data: str) -> ColorPrimaries:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColorPrimaries value: {data!r}")
    return cast(ColorPrimaries, data)
