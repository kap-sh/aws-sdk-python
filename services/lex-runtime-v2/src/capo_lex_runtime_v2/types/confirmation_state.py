"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ConfirmationState``."""

from typing import Literal, TypeAlias, cast

ConfirmationState: TypeAlias = Literal[
    "Confirmed",
    "Denied",
    "None",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfirmationState) -> str:
    return value


def deserialize_json(data: str) -> ConfirmationState:
    return cast(ConfirmationState, data)
