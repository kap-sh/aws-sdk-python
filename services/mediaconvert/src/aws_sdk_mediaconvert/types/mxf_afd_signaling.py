"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MxfAfdSignaling``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Optional. When you have AFD signaling set up in your output video stream, use this setting to choose whether to also include it in the MXF wrapper. Choose Don't copy to exclude AFD signaling from the MXF wrapper. Choose Copy from video stream to copy the AFD values from the video stream for this output to the MXF wrapper. Regardless of which option you choose, the AFD values remain in the video stream. Related settings: To set up your output to include or exclude AFD values, see AfdSignaling, under VideoDescription. On the console, find AFD signaling under the output's video encoding settings."""
MxfAfdSignaling: TypeAlias = Literal[
    "NO_COPY",
    "COPY_FROM_VIDEO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NO_COPY",
        "COPY_FROM_VIDEO",
    )
)


def serialize_json(value: MxfAfdSignaling) -> str:
    return value


def deserialize_json(data: str) -> MxfAfdSignaling:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MxfAfdSignaling value: {data!r}")
    return cast(MxfAfdSignaling, data)
