"""Generated from Smithy shape ``com.amazonaws.iot#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "DEVICE_CERTIFICATE",
    "CA_CERTIFICATE",
    "IOT_POLICY",
    "COGNITO_IDENTITY_POOL",
    "CLIENT_ID",
    "ACCOUNT_SETTINGS",
    "ROLE_ALIAS",
    "IAM_ROLE",
    "ISSUER_CERTIFICATE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEVICE_CERTIFICATE",
        "CA_CERTIFICATE",
        "IOT_POLICY",
        "COGNITO_IDENTITY_POOL",
        "CLIENT_ID",
        "ACCOUNT_SETTINGS",
        "ROLE_ALIAS",
        "IAM_ROLE",
        "ISSUER_CERTIFICATE",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
