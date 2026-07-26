"""Generated from Smithy shape ``com.amazonaws.amplifybackend#OAuthGrantType``."""

from typing import Literal, TypeAlias, cast

OAuthGrantType: TypeAlias = Literal[
    "CODE",
    "IMPLICIT",
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthGrantType) -> str:
    return value


def deserialize_json(data: str) -> OAuthGrantType:
    return cast(OAuthGrantType, data)
