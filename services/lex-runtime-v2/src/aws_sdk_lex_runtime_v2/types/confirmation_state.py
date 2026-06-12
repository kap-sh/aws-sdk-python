"""Generated from Smithy shape ``com.amazonaws.lexruntimev2#ConfirmationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_v2.errors import DeserializationError

ConfirmationState: TypeAlias = Literal[
    "Confirmed",
    "Denied",
    "None",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Confirmed",
        "Denied",
        "None",
    )
)


def serialize_json(value: ConfirmationState) -> str:
    return value


def deserialize_json(data: str) -> ConfirmationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfirmationState value: {data!r}")
    return cast(ConfirmationState, data)
