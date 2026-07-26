"""Generated from Smithy shape ``com.amazonaws.medialive#EbuTtDDestinationStyleControl``."""

from typing import Literal, TypeAlias, cast

"""Ebu Tt DDestination Style Control"""
EbuTtDDestinationStyleControl: TypeAlias = Literal[
    "EXCLUDE",
    "INCLUDE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EbuTtDDestinationStyleControl) -> str:
    return value


def deserialize_json(data: str) -> EbuTtDDestinationStyleControl:
    return cast(EbuTtDDestinationStyleControl, data)
