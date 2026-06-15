"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

CredentialProviderType: TypeAlias = Literal[
    "GATEWAY_IAM_ROLE",
    "OAUTH",
    "API_KEY",
    "CALLER_IAM_CREDENTIALS",
    "JWT_PASSTHROUGH",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "GATEWAY_IAM_ROLE",
        "OAUTH",
        "API_KEY",
        "CALLER_IAM_CREDENTIALS",
        "JWT_PASSTHROUGH",
    )
)


def serialize_json(value: CredentialProviderType) -> str:
    return value


def deserialize_json(data: str) -> CredentialProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CredentialProviderType value: {data!r}")
    return cast(CredentialProviderType, data)
