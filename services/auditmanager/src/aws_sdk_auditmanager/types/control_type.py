"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ControlType: TypeAlias = Literal[
    "Standard",
    "Custom",
    "Core",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "Custom",
        "Core",
    )
)


def serialize_json(value: ControlType) -> str:
    return value


def deserialize_json(data: str) -> ControlType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlType value: {data!r}")
    return cast(ControlType, data)
