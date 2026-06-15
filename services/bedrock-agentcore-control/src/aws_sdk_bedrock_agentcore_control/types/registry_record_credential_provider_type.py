"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryRecordCredentialProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

RegistryRecordCredentialProviderType: TypeAlias = Literal[
    "OAUTH",
    "IAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OAUTH",
        "IAM",
    )
)


def serialize_json(value: RegistryRecordCredentialProviderType) -> str:
    return value


def deserialize_json(data: str) -> RegistryRecordCredentialProviderType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RegistryRecordCredentialProviderType value: {data!r}"
        )
    return cast(RegistryRecordCredentialProviderType, data)
