"""Generated from Smithy shape ``com.amazonaws.datazone#OAuth2GrantType``."""

from typing import Literal, TypeAlias, cast

OAuth2GrantType: TypeAlias = Literal[
    "AUTHORIZATION_CODE",
    "CLIENT_CREDENTIALS",
    "JWT_BEARER",
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2GrantType) -> str:
    return value


def deserialize_json(data: str) -> OAuth2GrantType:
    return cast(OAuth2GrantType, data)
