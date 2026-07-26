"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2Syntax``."""

from typing import Literal, TypeAlias, cast

"""Specify whether this output's video uses the D10 syntax. Keep the default value to not use the syntax. Related settings: When you choose D10 for your MXF profile, you must also set this value to D10."""
Mpeg2Syntax: TypeAlias = Literal[
    "DEFAULT",
    "D_10",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2Syntax) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2Syntax:
    return cast(Mpeg2Syntax, data)
