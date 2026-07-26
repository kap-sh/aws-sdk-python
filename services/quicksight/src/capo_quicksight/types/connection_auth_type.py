"""Generated from Smithy shape ``com.amazonaws.quicksight#ConnectionAuthType``."""

from typing import Literal, TypeAlias, cast

ConnectionAuthType: TypeAlias = Literal[
    "BASIC",
    "API_KEY",
    "OAUTH2_CLIENT_CREDENTIALS",
    "NONE",
    "IAM",
    "OAUTH2_AUTHORIZATION_CODE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectionAuthType) -> str:
    return value


def deserialize_json(data: str) -> ConnectionAuthType:
    return cast(ConnectionAuthType, data)
