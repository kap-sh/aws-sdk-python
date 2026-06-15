"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OAuthGrantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

OAuthGrantType: TypeAlias = Literal[
    "CLIENT_CREDENTIALS",
    "AUTHORIZATION_CODE",
    "TOKEN_EXCHANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLIENT_CREDENTIALS",
        "AUTHORIZATION_CODE",
        "TOKEN_EXCHANGE",
    )
)


def serialize_json(value: OAuthGrantType) -> str:
    return value


def deserialize_json(data: str) -> OAuthGrantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OAuthGrantType value: {data!r}")
    return cast(OAuthGrantType, data)
