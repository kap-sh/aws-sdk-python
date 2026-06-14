"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClientAuthenticationMethodType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

ClientAuthenticationMethodType: TypeAlias = Literal[
    "CLIENT_SECRET_BASIC",
    "CLIENT_SECRET_POST",
    "AWS_IAM_ID_TOKEN_JWT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLIENT_SECRET_BASIC",
        "CLIENT_SECRET_POST",
        "AWS_IAM_ID_TOKEN_JWT",
    )
)


def serialize_json(value: ClientAuthenticationMethodType) -> str:
    return value


def deserialize_json(data: str) -> ClientAuthenticationMethodType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ClientAuthenticationMethodType value: {data!r}"
        )
    return cast(ClientAuthenticationMethodType, data)
