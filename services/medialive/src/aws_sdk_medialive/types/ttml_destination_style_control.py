"""Generated from Smithy shape ``com.amazonaws.medialive#TtmlDestinationStyleControl``."""

from typing import Literal, TypeAlias, cast

"""Ttml Destination Style Control"""
TtmlDestinationStyleControl: TypeAlias = Literal[
    "PASSTHROUGH",
    "USE_CONFIGURED",
]


# --- restJson1 ser/de ---
def serialize_json(value: TtmlDestinationStyleControl) -> str:
    return value


def deserialize_json(data: str) -> TtmlDestinationStyleControl:
    return cast(TtmlDestinationStyleControl, data)
