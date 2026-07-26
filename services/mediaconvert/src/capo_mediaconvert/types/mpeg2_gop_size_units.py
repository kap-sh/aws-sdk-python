"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Mpeg2GopSizeUnits``."""

from typing import Literal, TypeAlias, cast

"""Specify the units for GOP size. If you don't specify a value here, by default the encoder measures GOP size in frames."""
Mpeg2GopSizeUnits: TypeAlias = Literal[
    "FRAMES",
    "SECONDS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mpeg2GopSizeUnits) -> str:
    return value


def deserialize_json(data: str) -> Mpeg2GopSizeUnits:
    return cast(Mpeg2GopSizeUnits, data)
