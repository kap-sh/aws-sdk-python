"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TimecodeTrack``."""

from typing import Literal, TypeAlias, cast

"""To include a timecode track in your MP4 output: Choose Enabled. MediaConvert writes the timecode track in the Null Media Header box (NMHD), without any timecode text formatting information. You can also specify dropframe or non-dropframe timecode under the Drop Frame Timecode setting. To not include a timecode track: Keep the default value, Disabled."""
TimecodeTrack: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimecodeTrack) -> str:
    return value


def deserialize_json(data: str) -> TimecodeTrack:
    return cast(TimecodeTrack, data)
