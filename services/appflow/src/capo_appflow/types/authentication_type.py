"""Generated from Smithy shape ``com.amazonaws.appflow#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

AuthenticationType: TypeAlias = Literal[
    "OAUTH2",
    "APIKEY",
    "BASIC",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    return cast(AuthenticationType, data)
