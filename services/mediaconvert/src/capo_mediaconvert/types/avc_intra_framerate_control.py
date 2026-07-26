"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AvcIntraFramerateControl``."""

from typing import Literal, TypeAlias, cast

"""If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
AvcIntraFramerateControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AvcIntraFramerateControl) -> str:
    return value


def deserialize_json(data: str) -> AvcIntraFramerateControl:
    return cast(AvcIntraFramerateControl, data)
