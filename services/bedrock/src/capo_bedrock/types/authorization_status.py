"""Generated from Smithy shape ``com.amazonaws.bedrock#AuthorizationStatus``."""

from typing import Literal, TypeAlias, cast

AuthorizationStatus: TypeAlias = Literal[
    "AUTHORIZED",
    "NOT_AUTHORIZED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationStatus) -> str:
    return value


def deserialize_json(data: str) -> AuthorizationStatus:
    return cast(AuthorizationStatus, data)
