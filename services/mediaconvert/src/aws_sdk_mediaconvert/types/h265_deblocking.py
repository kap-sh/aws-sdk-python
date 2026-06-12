"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265Deblocking``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Use Deblocking to improve the video quality of your output by smoothing the edges of macroblock artifacts created during video compression. To reduce blocking artifacts at block boundaries, and improve overall video quality: Keep the default value, Enabled. To not apply any deblocking: Choose Disabled. Visible block edge artifacts might appear in the output, especially at lower bitrates."""
H265Deblocking: TypeAlias = Literal[
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


def serialize_json(value: H265Deblocking) -> str:
    return value


def deserialize_json(data: str) -> H265Deblocking:
    if data not in _VALUES:
        raise DeserializationError(f"unknown H265Deblocking value: {data!r}")
    return cast(H265Deblocking, data)
