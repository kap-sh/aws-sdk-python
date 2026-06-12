"""Generated from Smithy shape ``com.amazonaws.mediaconvert#SccDestinationFramerate``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Set Framerate to make sure that the captions and the video are synchronized in the output. Specify a frame rate that matches the frame rate of the associated video. If the video frame rate is 29.97, choose 29.97 dropframe only if the video has video_insertion=true and drop_frame_timecode=true; otherwise, choose 29.97 non-dropframe."""
SccDestinationFramerate: TypeAlias = Literal[
    "FRAMERATE_23_97",
    "FRAMERATE_24",
    "FRAMERATE_25",
    "FRAMERATE_29_97_DROPFRAME",
    "FRAMERATE_29_97_NON_DROPFRAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FRAMERATE_23_97",
        "FRAMERATE_24",
        "FRAMERATE_25",
        "FRAMERATE_29_97_DROPFRAME",
        "FRAMERATE_29_97_NON_DROPFRAME",
    )
)


def serialize_json(value: SccDestinationFramerate) -> str:
    return value


def deserialize_json(data: str) -> SccDestinationFramerate:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SccDestinationFramerate value: {data!r}")
    return cast(SccDestinationFramerate, data)
