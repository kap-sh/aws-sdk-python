"""Generated from Smithy shape ``com.amazonaws.iot#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

AuthenticationType: TypeAlias = Literal[
    "CUSTOM_AUTH_X509",
    "CUSTOM_AUTH",
    "AWS_X509",
    "AWS_SIGV4",
    "DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    return cast(AuthenticationType, data)
