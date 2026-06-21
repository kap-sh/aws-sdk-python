"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#DialogState``."""

from typing import Literal, TypeAlias, cast

DialogState: TypeAlias = Literal[
    "ElicitIntent",
    "ConfirmIntent",
    "ElicitSlot",
    "Fulfilled",
    "ReadyForFulfillment",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: DialogState) -> str:
    return value


def deserialize_json(data: str) -> DialogState:
    return cast(DialogState, data)
