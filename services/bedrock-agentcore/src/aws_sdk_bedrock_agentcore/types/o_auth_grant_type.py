"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#OAuthGrantType``."""

from typing import Literal, TypeAlias, cast

OAuthGrantType: TypeAlias = Literal[
    "CLIENT_CREDENTIALS",
    "AUTHORIZATION_CODE",
    "TOKEN_EXCHANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthGrantType) -> str:
    return value


def deserialize_json(data: str) -> OAuthGrantType:
    return cast(OAuthGrantType, data)
