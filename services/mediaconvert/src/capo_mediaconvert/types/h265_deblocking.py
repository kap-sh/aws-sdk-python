"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265Deblocking``."""

from typing import Literal, TypeAlias, cast

"""Use Deblocking to improve the video quality of your output by smoothing the edges of macroblock artifacts created during video compression. To reduce blocking artifacts at block boundaries, and improve overall video quality: Keep the default value, Enabled. To not apply any deblocking: Choose Disabled. Visible block edge artifacts might appear in the output, especially at lower bitrates."""
H265Deblocking: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265Deblocking) -> str:
    return value


def deserialize_json(data: str) -> H265Deblocking:
    return cast(H265Deblocking, data)
