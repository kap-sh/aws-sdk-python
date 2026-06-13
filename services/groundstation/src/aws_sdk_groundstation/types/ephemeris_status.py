"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

EphemerisStatus: TypeAlias = Literal[
    "VALIDATING",
    "INVALID",
    "ERROR",
    "ENABLED",
    "DISABLED",
    "EXPIRED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATING",
        "INVALID",
        "ERROR",
        "ENABLED",
        "DISABLED",
        "EXPIRED",
    )
)


def serialize_json(value: EphemerisStatus) -> str:
    return value


def deserialize_json(data: str) -> EphemerisStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EphemerisStatus value: {data!r}")
    return cast(EphemerisStatus, data)
