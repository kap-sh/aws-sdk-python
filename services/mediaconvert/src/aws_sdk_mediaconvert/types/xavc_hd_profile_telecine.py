"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcHdProfileTelecine``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Ignore this setting unless you set Frame rate (framerateNumerator divided by framerateDenominator) to 29.970. If your input framerate is 23.976, choose Hard. Otherwise, keep the default value None. For more information, see https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-telecine-and-inverse-telecine.html."""
XavcHdProfileTelecine: TypeAlias = Literal[
    "NONE",
    "HARD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "HARD",
    )
)


def serialize_json(value: XavcHdProfileTelecine) -> str:
    return value


def deserialize_json(data: str) -> XavcHdProfileTelecine:
    if data not in _VALUES:
        raise DeserializationError(f"unknown XavcHdProfileTelecine value: {data!r}")
    return cast(XavcHdProfileTelecine, data)
