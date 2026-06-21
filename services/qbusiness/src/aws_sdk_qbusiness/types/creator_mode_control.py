"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreatorModeControl``."""

from typing import Literal, TypeAlias, cast

CreatorModeControl: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CreatorModeControl) -> str:
    return value


def deserialize_json(data: str) -> CreatorModeControl:
    return cast(CreatorModeControl, data)
