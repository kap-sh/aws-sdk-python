"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

DiscoveryType: TypeAlias = Literal[
    "ZWAVE",
    "ZIGBEE",
    "CLOUD",
    "CUSTOM",
    "CONTROLLER_CAPABILITY_REDISCOVERY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ZWAVE",
        "ZIGBEE",
        "CLOUD",
        "CUSTOM",
        "CONTROLLER_CAPABILITY_REDISCOVERY",
    )
)


def serialize_json(value: DiscoveryType) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiscoveryType value: {data!r}")
    return cast(DiscoveryType, data)
