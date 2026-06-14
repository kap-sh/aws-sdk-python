"""Generated from Smithy shape ``com.amazonaws.datazone#OAuth2GrantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

OAuth2GrantType: TypeAlias = Literal[
    "AUTHORIZATION_CODE",
    "CLIENT_CREDENTIALS",
    "JWT_BEARER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTHORIZATION_CODE",
        "CLIENT_CREDENTIALS",
        "JWT_BEARER",
    )
)


def serialize_json(value: OAuth2GrantType) -> str:
    return value


def deserialize_json(data: str) -> OAuth2GrantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OAuth2GrantType value: {data!r}")
    return cast(OAuth2GrantType, data)
