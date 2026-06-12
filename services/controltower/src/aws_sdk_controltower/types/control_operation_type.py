"""Generated from Smithy shape ``com.amazonaws.controltower#ControlOperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controltower.errors import DeserializationError

ControlOperationType: TypeAlias = Literal[
    "ENABLE_CONTROL",
    "DISABLE_CONTROL",
    "UPDATE_ENABLED_CONTROL",
    "RESET_ENABLED_CONTROL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE_CONTROL",
        "DISABLE_CONTROL",
        "UPDATE_ENABLED_CONTROL",
        "RESET_ENABLED_CONTROL",
    )
)


def serialize_json(value: ControlOperationType) -> str:
    return value


def deserialize_json(data: str) -> ControlOperationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlOperationType value: {data!r}")
    return cast(ControlOperationType, data)
