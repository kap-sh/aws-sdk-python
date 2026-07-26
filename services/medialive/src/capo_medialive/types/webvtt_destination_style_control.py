"""Generated from Smithy shape ``com.amazonaws.medialive#WebvttDestinationStyleControl``."""

from typing import Literal, TypeAlias, cast

"""Webvtt Destination Style Control"""
WebvttDestinationStyleControl: TypeAlias = Literal[
    "NO_STYLE_DATA",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: WebvttDestinationStyleControl) -> str:
    return value


def deserialize_json(data: str) -> WebvttDestinationStyleControl:
    return cast(WebvttDestinationStyleControl, data)
