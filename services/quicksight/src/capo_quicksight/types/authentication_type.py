"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

AuthenticationType: TypeAlias = Literal[
    "PASSWORD",
    "KEYPAIR",
    "TOKEN",
    "X509",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    return cast(AuthenticationType, data)
