"""Generated from Smithy shape ``com.amazonaws.amplifybackend#Mode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifybackend.errors import DeserializationError

Mode: TypeAlias = Literal[
    "API_KEY",
    "AWS_IAM",
    "AMAZON_COGNITO_USER_POOLS",
    "OPENID_CONNECT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "API_KEY",
        "AWS_IAM",
        "AMAZON_COGNITO_USER_POOLS",
        "OPENID_CONNECT",
    )
)


def serialize_json(value: Mode) -> str:
    return value


def deserialize_json(data: str) -> Mode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Mode value: {data!r}")
    return cast(Mode, data)
