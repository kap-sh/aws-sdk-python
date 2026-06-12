"""Generated from Smithy shape ``com.amazonaws.iot#AutoRegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

AutoRegistrationStatus: TypeAlias = Literal[
    "ENABLE",
    "DISABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLE",
        "DISABLE",
    )
)


def serialize_json(value: AutoRegistrationStatus) -> str:
    return value


def deserialize_json(data: str) -> AutoRegistrationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoRegistrationStatus value: {data!r}")
    return cast(AutoRegistrationStatus, data)
