"""Generated from Smithy shape ``com.amazonaws.amplifybackend#OAuthGrantType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

OAuthGrantType: TypeAlias = Literal[
    "CODE",
    "IMPLICIT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CODE",
        "IMPLICIT",
    )
)


def serialize_json(value: OAuthGrantType) -> str:
    return value


def deserialize_json(data: str) -> OAuthGrantType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OAuthGrantType value: {data!r}")
    return cast(OAuthGrantType, data)
