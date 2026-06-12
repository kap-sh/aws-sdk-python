"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#DiscoveryAuthMaterialType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

DiscoveryAuthMaterialType: TypeAlias = Literal["ZWAVE_INSTALL_CODE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ZWAVE_INSTALL_CODE",))


def serialize_json(value: DiscoveryAuthMaterialType) -> str:
    return value


def deserialize_json(data: str) -> DiscoveryAuthMaterialType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DiscoveryAuthMaterialType value: {data!r}")
    return cast(DiscoveryAuthMaterialType, data)
