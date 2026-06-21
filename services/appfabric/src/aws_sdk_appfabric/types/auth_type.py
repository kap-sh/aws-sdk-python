"""Generated from Smithy shape ``com.amazonaws.appfabric#AuthType``."""

from typing import Literal, TypeAlias, cast

AuthType: TypeAlias = Literal[
    "oauth2",
    "apiKey",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthType) -> str:
    return value


def deserialize_json(data: str) -> AuthType:
    return cast(AuthType, data)
