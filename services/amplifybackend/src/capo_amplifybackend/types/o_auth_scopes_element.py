"""Generated from Smithy shape ``com.amazonaws.amplifybackend#OAuthScopesElement``."""

from typing import Literal, TypeAlias, cast

OAuthScopesElement: TypeAlias = Literal[
    "PHONE",
    "EMAIL",
    "OPENID",
    "PROFILE",
    "AWS_COGNITO_SIGNIN_USER_ADMIN",
]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthScopesElement) -> str:
    return value


def deserialize_json(data: str) -> OAuthScopesElement:
    return cast(OAuthScopesElement, data)
