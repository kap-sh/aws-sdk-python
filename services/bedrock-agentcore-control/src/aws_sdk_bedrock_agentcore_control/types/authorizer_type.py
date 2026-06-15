"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AuthorizerType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

AuthorizerType: TypeAlias = Literal[
    "CUSTOM_JWT",
    "AWS_IAM",
    "NONE",
    "AUTHENTICATE_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOM_JWT",
        "AWS_IAM",
        "NONE",
        "AUTHENTICATE_ONLY",
    )
)


def serialize_json(value: AuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthorizerType value: {data!r}")
    return cast(AuthorizerType, data)
