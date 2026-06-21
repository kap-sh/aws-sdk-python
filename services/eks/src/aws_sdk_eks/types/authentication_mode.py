"""Generated from Smithy shape ``com.amazonaws.eks#AuthenticationMode``."""

from typing import Literal, TypeAlias, cast

AuthenticationMode: TypeAlias = Literal[
    "API",
    "API_AND_CONFIG_MAP",
    "CONFIG_MAP",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationMode) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationMode:
    return cast(AuthenticationMode, data)
