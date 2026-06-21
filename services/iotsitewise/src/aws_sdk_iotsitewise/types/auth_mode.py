"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AuthMode``."""

from typing import Literal, TypeAlias, cast

AuthMode: TypeAlias = Literal[
    "IAM",
    "SSO",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthMode) -> str:
    return value


def deserialize_json(data: str) -> AuthMode:
    return cast(AuthMode, data)
