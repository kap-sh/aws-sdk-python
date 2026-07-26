"""Generated from Smithy shape ``com.amazonaws.mediaconvert#InputTimecodeSource``."""

from typing import Literal, TypeAlias, cast

"""Use this Timecode source setting, located under the input settings, to specify how the service counts input video frames. This input frame count affects only the behavior of features that apply to a single input at a time, such as input clipping and synchronizing some captions formats. Choose Embedded to use the timecodes in your input video. Choose Start at zero to start the first frame at zero. Choose Specified start to start the first frame at the timecode that you specify in the setting Start timecode. If you don't specify a value for Timecode source, the service will use Embedded by default. For more information about timecodes, see https://docs.aws.amazon.com/console/mediaconvert/timecode."""
InputTimecodeSource: TypeAlias = Literal[
    "EMBEDDED",
    "ZEROBASED",
    "SPECIFIEDSTART",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputTimecodeSource) -> str:
    return value


def deserialize_json(data: str) -> InputTimecodeSource:
    return cast(InputTimecodeSource, data)
