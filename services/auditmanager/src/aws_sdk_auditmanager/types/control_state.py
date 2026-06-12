"""Generated from Smithy shape ``com.amazonaws.auditmanager#ControlState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

ControlState: TypeAlias = Literal[
    "ACTIVE",
    "END_OF_SUPPORT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "END_OF_SUPPORT",
    )
)


def serialize_json(value: ControlState) -> str:
    return value


def deserialize_json(data: str) -> ControlState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlState value: {data!r}")
    return cast(ControlState, data)
