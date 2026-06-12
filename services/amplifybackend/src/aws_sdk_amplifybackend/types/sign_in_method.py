"""Generated from Smithy shape ``com.amazonaws.amplifybackend#SignInMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

SignInMethod: TypeAlias = Literal[
    "EMAIL",
    "EMAIL_AND_PHONE_NUMBER",
    "PHONE_NUMBER",
    "USERNAME",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EMAIL",
        "EMAIL_AND_PHONE_NUMBER",
        "PHONE_NUMBER",
        "USERNAME",
    )
)


def serialize_json(value: SignInMethod) -> str:
    return value


def deserialize_json(data: str) -> SignInMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SignInMethod value: {data!r}")
    return cast(SignInMethod, data)
