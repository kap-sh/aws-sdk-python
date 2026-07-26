"""Generated from Smithy shape ``com.amazonaws.amplifybackend#SignInMethod``."""

from typing import Literal, TypeAlias, cast

SignInMethod: TypeAlias = Literal[
    "EMAIL",
    "EMAIL_AND_PHONE_NUMBER",
    "PHONE_NUMBER",
    "USERNAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignInMethod) -> str:
    return value


def deserialize_json(data: str) -> SignInMethod:
    return cast(SignInMethod, data)
