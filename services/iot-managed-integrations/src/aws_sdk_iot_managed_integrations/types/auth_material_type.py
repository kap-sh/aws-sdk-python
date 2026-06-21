"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#AuthMaterialType``."""

from typing import Literal, TypeAlias, cast

AuthMaterialType: TypeAlias = Literal[
    "CUSTOM_PROTOCOL_QR_BAR_CODE",
    "WIFI_SETUP_QR_BAR_CODE",
    "ZWAVE_QR_BAR_CODE",
    "ZIGBEE_QR_BAR_CODE",
    "DISCOVERED_DEVICE",
    "PRE_ONBOARDED_CLOUD",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthMaterialType) -> str:
    return value


def deserialize_json(data: str) -> AuthMaterialType:
    return cast(AuthMaterialType, data)
