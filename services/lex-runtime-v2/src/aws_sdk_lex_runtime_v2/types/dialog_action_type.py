"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#DialogActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

DialogActionType: TypeAlias = Literal[
    "Close",
    "ConfirmIntent",
    "Delegate",
    "ElicitIntent",
    "ElicitSlot",
    "None",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Close",
        "ConfirmIntent",
        "Delegate",
        "ElicitIntent",
        "ElicitSlot",
        "None",
    )
)


def serialize_json(value: DialogActionType) -> str:
    return value


def deserialize_json(data: str) -> DialogActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DialogActionType value: {data!r}")
    return cast(DialogActionType, data)
