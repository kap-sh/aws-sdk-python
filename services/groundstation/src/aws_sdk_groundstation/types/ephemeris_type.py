"""Generated from Smithy shape ``com.amazonaws.groundstation#EphemerisType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

EphemerisType: TypeAlias = Literal[
    "TLE",
    "OEM",
    "AZ_EL",
    "SERVICE_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TLE",
        "OEM",
        "AZ_EL",
        "SERVICE_MANAGED",
    )
)


def serialize_json(value: EphemerisType) -> str:
    return value


def deserialize_json(data: str) -> EphemerisType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EphemerisType value: {data!r}")
    return cast(EphemerisType, data)
