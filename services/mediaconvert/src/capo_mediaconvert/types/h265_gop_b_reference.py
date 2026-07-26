"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265GopBReference``."""

from typing import Literal, TypeAlias, cast

"""Specify whether to allow B-frames to be referenced by other frame types. To use reference B-frames when your GOP structure has 1 or more B-frames: Leave blank or keep the default value Enabled. We recommend that you choose Enabled to help improve the video quality of your output relative to its bitrate. To not use reference B-frames: Choose Disabled."""
H265GopBReference: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265GopBReference) -> str:
    return value


def deserialize_json(data: str) -> H265GopBReference:
    return cast(H265GopBReference, data)
