"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3SurroundMode``."""

from typing import Literal, TypeAlias, cast

"""When encoding 2/0 audio, sets whether Dolby Surround is matrix encoded into the two channels."""
Eac3SurroundMode: TypeAlias = Literal[
    "NOT_INDICATED",
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3SurroundMode) -> str:
    return value


def deserialize_json(data: str) -> Eac3SurroundMode:
    return cast(Eac3SurroundMode, data)
