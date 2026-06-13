"""Generated from Smithy shape ``com.amazonaws.groundstation#CapabilityHealth``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

CapabilityHealth: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
    )
)


def serialize_json(value: CapabilityHealth) -> str:
    return value


def deserialize_json(data: str) -> CapabilityHealth:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapabilityHealth value: {data!r}")
    return cast(CapabilityHealth, data)
