"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#DialogState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_service.errors import DeserializationError

DialogState: TypeAlias = Literal[
    "ElicitIntent",
    "ConfirmIntent",
    "ElicitSlot",
    "Fulfilled",
    "ReadyForFulfillment",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ElicitIntent",
        "ConfirmIntent",
        "ElicitSlot",
        "Fulfilled",
        "ReadyForFulfillment",
        "Failed",
    )
)


def serialize_json(value: DialogState) -> str:
    return value


def deserialize_json(data: str) -> DialogState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DialogState value: {data!r}")
    return cast(DialogState, data)
