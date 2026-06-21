"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Eac3DcFilter``."""

from typing import Literal, TypeAlias, cast

"""Activates a DC highpass filter for all input channels."""
Eac3DcFilter: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Eac3DcFilter) -> str:
    return value


def deserialize_json(data: str) -> Eac3DcFilter:
    return cast(Eac3DcFilter, data)
