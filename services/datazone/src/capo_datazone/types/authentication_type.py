"""Generated from Smithy shape ``com.amazonaws.datazone#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

AuthenticationType: TypeAlias = Literal[
    "BASIC",
    "OAUTH2",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    return cast(AuthenticationType, data)
