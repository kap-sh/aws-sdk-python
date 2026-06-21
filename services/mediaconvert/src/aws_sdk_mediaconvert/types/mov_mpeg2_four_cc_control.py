"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovMpeg2FourCCControl``."""

from typing import Literal, TypeAlias, cast

"""When set to XDCAM, writes MPEG2 video streams into the QuickTime file using XDCAM fourcc codes. This increases compatibility with Apple editors and players, but may decrease compatibility with other players. Only applicable when the video codec is MPEG2."""
MovMpeg2FourCCControl: TypeAlias = Literal[
    "XDCAM",
    "MPEG",
]


# --- restJson1 ser/de ---
def serialize_json(value: MovMpeg2FourCCControl) -> str:
    return value


def deserialize_json(data: str) -> MovMpeg2FourCCControl:
    return cast(MovMpeg2FourCCControl, data)
