"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Oauth2FlowType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore.errors import DeserializationError

Oauth2FlowType: TypeAlias = Literal[
    "USER_FEDERATION",
    "M2M",
    "ON_BEHALF_OF_TOKEN_EXCHANGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_FEDERATION",
        "M2M",
        "ON_BEHALF_OF_TOKEN_EXCHANGE",
    )
)


def serialize_json(value: Oauth2FlowType) -> str:
    return value


def deserialize_json(data: str) -> Oauth2FlowType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Oauth2FlowType value: {data!r}")
    return cast(Oauth2FlowType, data)
