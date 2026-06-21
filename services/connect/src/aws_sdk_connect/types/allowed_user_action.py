"""Generated from Smithy shape ``com.amazonaws.connect#AllowedUserAction``."""

from typing import Literal, TypeAlias, cast

AllowedUserAction: TypeAlias = Literal[
    "CALL",
    "DISCARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedUserAction) -> str:
    return value


def deserialize_json(data: str) -> AllowedUserAction:
    return cast(AllowedUserAction, data)
