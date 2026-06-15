"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#OnBehalfOfTokenExchangeGrantTypeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

OnBehalfOfTokenExchangeGrantTypeType: TypeAlias = Literal[
    "TOKEN_EXCHANGE",
    "JWT_AUTHORIZATION_GRANT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOKEN_EXCHANGE",
        "JWT_AUTHORIZATION_GRANT",
    )
)


def serialize_json(value: OnBehalfOfTokenExchangeGrantTypeType) -> str:
    return value


def deserialize_json(data: str) -> OnBehalfOfTokenExchangeGrantTypeType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OnBehalfOfTokenExchangeGrantTypeType value: {data!r}"
        )
    return cast(OnBehalfOfTokenExchangeGrantTypeType, data)
