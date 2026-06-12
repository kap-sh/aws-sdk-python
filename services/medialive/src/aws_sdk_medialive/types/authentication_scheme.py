"""Generated from Smithy shape ``com.amazonaws.medialive#AuthenticationScheme``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Authentication Scheme"""
AuthenticationScheme: TypeAlias = Literal[
    "AKAMAI",
    "COMMON",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AKAMAI",
        "COMMON",
    )
)


def serialize_json(value: AuthenticationScheme) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationScheme:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationScheme value: {data!r}")
    return cast(AuthenticationScheme, data)
