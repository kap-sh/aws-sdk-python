"""Generated from Smithy shape ``com.amazonaws.pinpoint#ButtonAction``."""

from typing import Literal, TypeAlias, cast

ButtonAction: TypeAlias = Literal[
    "LINK",
    "DEEP_LINK",
    "CLOSE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ButtonAction) -> str:
    return value


def deserialize_json(data: str) -> ButtonAction:
    return cast(ButtonAction, data)
