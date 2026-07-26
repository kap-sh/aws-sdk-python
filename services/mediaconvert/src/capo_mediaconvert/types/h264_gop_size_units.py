"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H264GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

"""Specify how the transcoder determines GOP size for this output. We recommend that you have the transcoder automatically choose this value for you based on characteristics of your input video. To enable this automatic behavior, choose Auto and and leave GOP size blank. By default, if you don't specify GOP mode control, MediaConvert will use automatic behavior. If your output group specifies HLS, DASH, or CMAF, set GOP mode control to Auto and leave GOP size blank in each output in your output group. To explicitly specify the GOP length, choose Specified, frames or Specified, seconds and then provide the GOP length in the related setting GOP size."""
H264GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
    "AUTO",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> H264GopSizeUnits:
    return cast(H264GopSizeUnits, data)
