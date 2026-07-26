"""Generated from Smithy shape ``com.amazonaws.medialive#AuthenticationScheme``."""

from typing import Literal, TypeAlias, cast

"""Authentication Scheme"""
AuthenticationScheme: TypeAlias = Literal[
    "AKAMAI",
    "COMMON",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationScheme) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationScheme:
    return cast(AuthenticationScheme, data)
