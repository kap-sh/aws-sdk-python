"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vc3Class``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specify the VC3 class to choose the quality characteristics for this output. VC3 class, together with the settings Framerate (framerateNumerator and framerateDenominator) and Resolution (height and width), determine your output bitrate. For example, say that your video resolution is 1920x1080 and your framerate is 29.97. Then Class 145 gives you an output with a bitrate of approximately 145 Mbps and Class 220 gives you and output with a bitrate of approximately 220 Mbps. VC3 class also specifies the color bit depth of your output."""
Vc3Class: TypeAlias = Literal[
    "CLASS_145_8BIT",
    "CLASS_220_8BIT",
    "CLASS_220_10BIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLASS_145_8BIT",
        "CLASS_220_8BIT",
        "CLASS_220_10BIT",
    )
)


def serialize_json(value: Vc3Class) -> str:
    return value


def deserialize_json(data: str) -> Vc3Class:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Vc3Class value: {data!r}")
    return cast(Vc3Class, data)
