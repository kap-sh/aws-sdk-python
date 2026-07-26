"""Generated from Smithy shape ``com.amazonaws.iot#ResourceType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
