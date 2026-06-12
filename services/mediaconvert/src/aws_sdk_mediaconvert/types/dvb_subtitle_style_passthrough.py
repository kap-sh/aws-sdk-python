"""Generated from Smithy shape ``com.amazonaws.mediaconvert#DvbSubtitleStylePassthrough``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""To use the available style, color, and position information from your input captions: Set Style passthrough to Enabled. Note that MediaConvert uses default settings for any missing style or position information in your input captions To ignore the style and position information from your input captions and use default settings: Leave blank or keep the default value, Disabled. Default settings include white text with black outlining, bottom-center positioning, and automatic sizing. Whether you set Style passthrough to enabled or not, you can also choose to manually override any of the individual style and position settings. You can also override any fonts by manually specifying custom font files."""
DvbSubtitleStylePassthrough: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DvbSubtitleStylePassthrough) -> str:
    return value


def deserialize_json(data: str) -> DvbSubtitleStylePassthrough:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DvbSubtitleStylePassthrough value: {data!r}"
        )
    return cast(DvbSubtitleStylePassthrough, data)
