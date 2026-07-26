"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MovClapAtom``."""

from typing import Literal, TypeAlias, cast

"""When enabled, include 'clap' atom if appropriate for the video output settings."""
MovClapAtom: TypeAlias = Literal[
    "INCLUDE",
    "EXCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MovClapAtom) -> str:
    return value


def deserialize_json(data: str) -> MovClapAtom:
    return cast(MovClapAtom, data)
