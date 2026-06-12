"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovMpeg2FourCCControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2."""
MovMpeg2FourCCControl: TypeAlias = Literal[
    "XDCAM",
    "MPEG",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "XDCAM",
        "MPEG",
    )
)


def serialize_json(value: MovMpeg2FourCCControl) -> str:
    return value


def deserialize_json(data: str) -> MovMpeg2FourCCControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MovMpeg2FourCCControl value: {data!r}")
    return cast(MovMpeg2FourCCControl, data)
