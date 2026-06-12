"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VideoTimecodeInsertion``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Applies only to H.264, H.265, MPEG2, and ProRes outputs. Only enable Timecode insertion when the input frame rate is identical to the output frame rate. To include timecodes in this output, set Timecode insertion to PIC_TIMING_SEI. To leave them out, set it to DISABLED. Default is DISABLED. When the service inserts timecodes in an output, by default, it uses any embedded timecodes from the input. If none are present, the service will set the timecode for the first output frame to zero. To change this default behavior, adjust the settings under Timecode configuration. In the console, these settings are located under Job > Job settings > Timecode configuration. Note - Timecode source under input settings does not affect the timecodes that are inserted in the output. Source under Job settings > Timecode configuration does."""
VideoTimecodeInsertion: TypeAlias = Literal[
    "DISABLED",
    "PIC_TIMING_SEI",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "PIC_TIMING_SEI",
    )
)


def serialize_json(value: VideoTimecodeInsertion) -> str:
    return value


def deserialize_json(data: str) -> VideoTimecodeInsertion:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VideoTimecodeInsertion value: {data!r}")
    return cast(VideoTimecodeInsertion, data)
