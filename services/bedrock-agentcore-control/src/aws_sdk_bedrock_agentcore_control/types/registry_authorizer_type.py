"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#RegistryAuthorizerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

RegistryAuthorizerType: TypeAlias = Literal[
    "CUSTOM_JWT",
    "AWS_IAM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM_JWT",
        "AWS_IAM",
    )
)


def serialize_json(value: RegistryAuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> RegistryAuthorizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegistryAuthorizerType value: {data!r}")
    return cast(RegistryAuthorizerType, data)
