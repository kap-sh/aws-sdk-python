"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreatorModeControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

CreatorModeControl: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: CreatorModeControl) -> str:
    return value


def deserialize_json(data: str) -> CreatorModeControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CreatorModeControl value: {data!r}")
    return cast(CreatorModeControl, data)
