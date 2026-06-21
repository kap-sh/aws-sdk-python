"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveryAuthMaterialType``."""

from typing import Literal, TypeAlias, cast

DiscoveryAuthMaterialType: TypeAlias = Literal["ZWAVE_INSTALL_CODE",]


# --- restJson1 ser/de ---
def serialize_json(value: DiscoveryAuthMaterialType) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryAuthMaterialType:
    return cast(DiscoveryAuthMaterialType, data)
