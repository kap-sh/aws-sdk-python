"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DialogActionType``."""

from typing import Literal, TypeAlias, cast

DialogActionType: TypeAlias = Literal[
    "ElicitIntent",
    "StartIntent",
    "ElicitSlot",
    "EvaluateConditional",
    "InvokeDialogCodeHook",
    "ConfirmIntent",
    "FulfillIntent",
    "CloseIntent",
    "EndConversation",
]


# --- restJson1 ser/de ---
def serialize_json(value: DialogActionType) -> str:
    return value


def deserialize_json(data: str) -> DialogActionType:
    return cast(DialogActionType, data)
