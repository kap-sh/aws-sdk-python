"""Generated from Smithy shape ``com.amazonaws.iotwireless#PositionConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_wireless.errors import DeserializationError

PositionConfigurationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_json(value: PositionConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> PositionConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PositionConfigurationStatus value: {data!r}"
        )
    return cast(PositionConfigurationStatus, data)
