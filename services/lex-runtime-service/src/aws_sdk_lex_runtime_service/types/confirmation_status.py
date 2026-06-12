"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#ConfirmationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lex_runtime_service.errors import DeserializationError

ConfirmationStatus: TypeAlias = Literal[
    "None",
    "Confirmed",
    "Denied",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "None",
        "Confirmed",
        "Denied",
    )
)


def serialize_json(value: ConfirmationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfirmationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfirmationStatus value: {data!r}")
    return cast(ConfirmationStatus, data)
