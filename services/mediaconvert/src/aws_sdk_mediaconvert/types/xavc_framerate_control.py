"""Generated from Smithy shape ``com.amazonaws.mediaconvert#XavcFramerateControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""If you are using the console, use the Frame rate setting to specify the frame rate for this output. If you want to keep the same frame rate as the input video, choose Follow source. If you want to do frame rate conversion, choose a frame rate from the dropdown list. The framerates shown in the dropdown list are decimal approximations of fractions."""
XavcFramerateControl: TypeAlias = Literal[
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


def serialize_json(value: XavcFramerateControl) -> str:
    return value


def deserialize_json(data: str) -> XavcFramerateControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown XavcFramerateControl value: {data!r}")
    return cast(XavcFramerateControl, data)
