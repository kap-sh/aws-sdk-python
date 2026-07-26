"""Generated from Smithy shape ``com.amazonaws.imagebuilder#Platform``."""

from typing import Literal, TypeAlias, cast

Platform: TypeAlias = Literal[
    "Windows",
    "Linux",
    "macOS",
]


# --- restJson1 ser/de ---
def serialize_json(value: Platform) -> str:
    return value


def deserialize_json(data: str) -> Platform:
    return cast(Platform, data)
