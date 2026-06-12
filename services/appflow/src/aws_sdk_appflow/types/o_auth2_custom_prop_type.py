"""Generated from Smithy shape ``com.amazonaws.appflow#OAuth2CustomPropType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appflow.errors import DeserializationError

OAuth2CustomPropType: TypeAlias = Literal[
    "TOKEN_URL",
    "AUTH_URL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TOKEN_URL",
        "AUTH_URL",
    )
)


def serialize_json(value: OAuth2CustomPropType) -> str:
    return value


def deserialize_json(data: str) -> OAuth2CustomPropType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OAuth2CustomPropType value: {data!r}")
    return cast(OAuth2CustomPropType, data)
