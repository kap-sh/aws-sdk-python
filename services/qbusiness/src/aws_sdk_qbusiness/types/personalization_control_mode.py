"""Generated from Smithy shape ``com.amazonaws.qbusiness#PersonalizationControlMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

PersonalizationControlMode: TypeAlias = Literal[
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


def serialize_json(value: PersonalizationControlMode) -> str:
    return value


def deserialize_json(data: str) -> PersonalizationControlMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PersonalizationControlMode value: {data!r}"
        )
    return cast(PersonalizationControlMode, data)
