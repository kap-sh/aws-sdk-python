"""Generated from Smithy shape ``com.amazonaws.auditmanager#FrameworkType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

FrameworkType: TypeAlias = Literal[
    "Standard",
    "Custom",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Standard",
        "Custom",
    )
)


def serialize_json(value: FrameworkType) -> str:
    return value


def deserialize_json(data: str) -> FrameworkType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FrameworkType value: {data!r}")
    return cast(FrameworkType, data)
