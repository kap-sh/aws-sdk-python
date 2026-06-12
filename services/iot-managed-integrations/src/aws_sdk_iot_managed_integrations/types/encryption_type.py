"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#EncryptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

EncryptionType: TypeAlias = Literal[
    "MANAGED_INTEGRATIONS_DEFAULT_ENCRYPTION",
    "CUSTOMER_KEY_ENCRYPTION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANAGED_INTEGRATIONS_DEFAULT_ENCRYPTION",
        "CUSTOMER_KEY_ENCRYPTION",
    )
)


def serialize_json(value: EncryptionType) -> str:
    return value


def deserialize_json(data: str) -> EncryptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionType value: {data!r}")
    return cast(EncryptionType, data)
