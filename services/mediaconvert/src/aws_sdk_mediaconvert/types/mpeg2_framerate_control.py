"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2FramerateControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
Mpeg2FramerateControl: TypeAlias = Literal[
    "INITIALIZE_FROM_SOURCE",
    "SPECIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIALIZE_FROM_SOURCE",
        "SPECIFIED",
    )
)


def serialize_json(value: Mpeg2FramerateControl) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2FramerateControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mpeg2FramerateControl value: {data!r}")
    return cast(Mpeg2FramerateControl, data)
