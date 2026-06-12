"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionConfigurationFec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

PositionConfigurationFec: TypeAlias = Literal[
    "ROSE",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ROSE",
        "NONE",
    )
)


def serialize_json(value: PositionConfigurationFec) -> str:
    return value


def deserialize_json(data: str) -> PositionConfigurationFec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PositionConfigurationFec value: {data!r}")
    return cast(PositionConfigurationFec, data)
