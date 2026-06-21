"""Generated from Smithy shape ``com.amazonaws.amplifybackend#AuthResources``."""

from typing import Literal, TypeAlias, cast

AuthResources: TypeAlias = Literal[
    "USER_POOL_ONLY",
    "IDENTITY_POOL_AND_USER_POOL",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthResources) -> str:
    return value


def deserialize_json(data: str) -> AuthResources:
    return cast(AuthResources, data)
