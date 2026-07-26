"""Generated from Smithy shape ``com.amazonaws.chime#License``."""

from typing import Literal, TypeAlias, cast

License: TypeAlias = Literal[
    "Basic",
    "Plus",
    "Pro",
    "ProTrial",
]


# --- restJson1 ser/de ---
def serialize_json(value: License) -> str:
    return value


def deserialize_json(data: str) -> License:
    return cast(License, data)
