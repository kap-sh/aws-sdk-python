"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DialogActionType``."""

from typing import Literal, TypeAlias, cast

DialogActionType: TypeAlias = Literal[
    "Close",
    "ConfirmIntent",
    "Delegate",
    "ElicitIntent",
    "ElicitSlot",
    "None",
]


# --- restJson1 ser/de ---
def serialize_json(value: DialogActionType) -> str:
    return value


def deserialize_json(data: str) -> DialogActionType:
    return cast(DialogActionType, data)
