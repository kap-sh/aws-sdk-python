"""Generated from Smithy shape ``com.amazonaws.appflow#OAuth2CustomPropType``."""

from typing import Literal, TypeAlias, cast

OAuth2CustomPropType: TypeAlias = Literal[
    "TOKEN_URL",
    "AUTH_URL",
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2CustomPropType) -> str:
    return value


def deserialize_json(data: str) -> OAuth2CustomPropType:
    return cast(OAuth2CustomPropType, data)
