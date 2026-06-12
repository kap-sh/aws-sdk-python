"""Generated from Smithy shape ``com.amazonaws.amplifybackend#OAuthScopesElement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

OAuthScopesElement: TypeAlias = Literal[
    "PHONE",
    "EMAIL",
    "OPENID",
    "PROFILE",
    "AWS_COGNITO_SIGNIN_USER_ADMIN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PHONE",
        "EMAIL",
        "OPENID",
        "PROFILE",
        "AWS_COGNITO_SIGNIN_USER_ADMIN",
    )
)


def serialize_json(value: OAuthScopesElement) -> str:
    return value


def deserialize_json(data: str) -> OAuthScopesElement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OAuthScopesElement value: {data!r}")
    return cast(OAuthScopesElement, data)
