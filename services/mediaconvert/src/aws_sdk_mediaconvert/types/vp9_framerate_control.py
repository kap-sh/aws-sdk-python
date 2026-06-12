"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Vp9FramerateControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If you are using the console, use the Framerate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list or choose Custom. The framerates shown in the dropdown list are decimal approximations of fractions. If you choose Custom, specify your frame rate as a fraction."""
Vp9FramerateControl: TypeAlias = Literal[
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


def serialize_json(value: Vp9FramerateControl) -> str:
    return value


def deserialize_json(data: str) -> Vp9FramerateControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Vp9FramerateControl value: {data!r}")
    return cast(Vp9FramerateControl, data)
