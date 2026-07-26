"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProviderType``."""

from typing import Literal, TypeAlias, cast

CredentialProviderType: TypeAlias = Literal[
    "GATEWAY_IAM_ROLE",
    "OAUTH",
    "API_KEY",
    "CALLER_IAM_CREDENTIALS",
    "JWT_PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: CredentialProviderType) -> str:
    return value


def deserialize_json(data: str) -> CredentialProviderType:
    return cast(CredentialProviderType, data)
