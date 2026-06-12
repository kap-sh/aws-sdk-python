"""Generated from Smithy shape ``com.amazonaws.amplifybackend#AuthResources``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

AuthResources: TypeAlias = Literal[
    "USER_POOL_ONLY",
    "IDENTITY_POOL_AND_USER_POOL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_POOL_ONLY",
        "IDENTITY_POOL_AND_USER_POOL",
    )
)


def serialize_json(value: AuthResources) -> str:
    return value


def deserialize_json(data: str) -> AuthResources:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthResources value: {data!r}")
    return cast(AuthResources, data)
