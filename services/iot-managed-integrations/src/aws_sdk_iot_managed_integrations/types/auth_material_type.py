"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthMaterialType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

AuthMaterialType: TypeAlias = Literal[
    "CUSTOM_PROTOCOL_QR_BAR_CODE",
    "WIFI_SETUP_QR_BAR_CODE",
    "ZWAVE_QR_BAR_CODE",
    "ZIGBEE_QR_BAR_CODE",
    "DISCOVERED_DEVICE",
    "PRE_ONBOARDED_CLOUD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM_PROTOCOL_QR_BAR_CODE",
        "WIFI_SETUP_QR_BAR_CODE",
        "ZWAVE_QR_BAR_CODE",
        "ZIGBEE_QR_BAR_CODE",
        "DISCOVERED_DEVICE",
        "PRE_ONBOARDED_CLOUD",
    )
)


def serialize_json(value: AuthMaterialType) -> str:
    return value


def deserialize_json(data: str) -> AuthMaterialType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthMaterialType value: {data!r}")
    return cast(AuthMaterialType, data)
