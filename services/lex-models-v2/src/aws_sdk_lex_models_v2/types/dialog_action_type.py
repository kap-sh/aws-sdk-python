"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DialogActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_models_v2.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "ElicitIntent",
        "StartIntent",
        "ElicitSlot",
        "EvaluateConditional",
        "InvokeDialogCodeHook",
        "ConfirmIntent",
        "FulfillIntent",
        "CloseIntent",
        "EndConversation",
    )
)


def serialize_json(value: DialogActionType) -> str:
    return value


def deserialize_json(data: str) -> DialogActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DialogActionType value: {data!r}")
    return cast(DialogActionType, data)
