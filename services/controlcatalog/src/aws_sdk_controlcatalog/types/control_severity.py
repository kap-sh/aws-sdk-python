"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlSeverity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controlcatalog.errors import DeserializationError

ControlSeverity: TypeAlias = Literal[
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LOW",
        "MEDIUM",
        "HIGH",
        "CRITICAL",
    )
)


def serialize_json(value: ControlSeverity) -> str:
    return value


def deserialize_json(data: str) -> ControlSeverity:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlSeverity value: {data!r}")
    return cast(ControlSeverity, data)
