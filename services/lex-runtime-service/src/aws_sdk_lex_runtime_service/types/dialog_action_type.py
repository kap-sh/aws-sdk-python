"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#DialogActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_service.errors import DeserializationError

DialogActionType: TypeAlias = Literal[
    "ElicitIntent",
    "ConfirmIntent",
    "ElicitSlot",
    "Close",
    "Delegate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ElicitIntent",
        "ConfirmIntent",
        "ElicitSlot",
        "Close",
        "Delegate",
    )
)


def serialize_json(value: DialogActionType) -> str:
    return value


def deserialize_json(data: str) -> DialogActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DialogActionType value: {data!r}")
    return cast(DialogActionType, data)
