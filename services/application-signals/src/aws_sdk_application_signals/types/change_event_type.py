"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ChangeEventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

ChangeEventType: TypeAlias = Literal[
    "DEPLOYMENT",
    "CONFIGURATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEPLOYMENT",
        "CONFIGURATION",
    )
)


def serialize_json(value: ChangeEventType) -> str:
    return value


def deserialize_json(data: str) -> ChangeEventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeEventType value: {data!r}")
    return cast(ChangeEventType, data)
