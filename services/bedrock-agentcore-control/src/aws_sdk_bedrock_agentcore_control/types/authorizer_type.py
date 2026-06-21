"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AuthorizerType``."""

from typing import Literal, TypeAlias, cast

AuthorizerType: TypeAlias = Literal[
    "CUSTOM_JWT",
    "AWS_IAM",
    "NONE",
    "AUTHENTICATE_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizerType) -> str:
    return value


def deserialize_json(data: str) -> AuthorizerType:
    return cast(AuthorizerType, data)
