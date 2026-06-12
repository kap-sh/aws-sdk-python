"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#ProtocolType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

ProtocolType: TypeAlias = Literal[
    "ZWAVE",
    "ZIGBEE",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ZWAVE",
        "ZIGBEE",
        "CUSTOM",
    )
)


def serialize_json(value: ProtocolType) -> str:
    return value


def deserialize_json(data: str) -> ProtocolType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProtocolType value: {data!r}")
    return cast(ProtocolType, data)
