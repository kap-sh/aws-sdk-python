"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#FallbackAction``."""

from typing import Literal, TypeAlias, cast

FallbackAction: TypeAlias = Literal[
    "CONTINUE",
    "ABORT",
]


# --- restJson1 ser/de ---
def serialize_json(value: FallbackAction) -> str:
    return value


def deserialize_json(data: str) -> FallbackAction:
    return cast(FallbackAction, data)
