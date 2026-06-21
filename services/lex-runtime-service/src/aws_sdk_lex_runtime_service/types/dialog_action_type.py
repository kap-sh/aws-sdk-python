"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#DialogActionType``."""

from typing import Literal, TypeAlias, cast

DialogActionType: TypeAlias = Literal[
    "ElicitIntent",
    "ConfirmIntent",
    "ElicitSlot",
    "Close",
    "Delegate",
]


# --- restJson1 ser/de ---
def serialize_json(value: DialogActionType) -> str:
    return value


def deserialize_json(data: str) -> DialogActionType:
    return cast(DialogActionType, data)
