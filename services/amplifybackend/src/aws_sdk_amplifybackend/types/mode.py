"""Generated from Smithy shape ``com.amazonaws.amplifybackend#Mode``."""

from typing import Literal, TypeAlias, cast

Mode: TypeAlias = Literal[
    "API_KEY",
    "AWS_IAM",
    "AMAZON_COGNITO_USER_POOLS",
    "OPENID_CONNECT",
]


# --- restJson1 ser/de ---
def serialize_json(value: Mode) -> str:
    return value


def deserialize_json(data: str) -> Mode:
    return cast(Mode, data)
