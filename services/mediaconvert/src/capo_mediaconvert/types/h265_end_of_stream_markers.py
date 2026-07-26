"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265EndOfStreamMarkers``."""

from typing import Literal, TypeAlias, cast

"""Optionally include or suppress markers at the end of your output that signal the end of the video stream. To include end of stream markers: Leave blank or keep the default value, Include. To not include end of stream markers: Choose Suppress. This is useful when your output will be inserted into another stream."""
H265EndOfStreamMarkers: TypeAlias = Literal[
    "INCLUDE",
    "SUPPRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265EndOfStreamMarkers) -> str:
    return value


def deserialize_json(data: str) -> H265EndOfStreamMarkers:
    return cast(H265EndOfStreamMarkers, data)
