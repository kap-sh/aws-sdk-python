"""Generated from Smithy shape ``com.amazonaws.appsync#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

AuthenticationType: TypeAlias = Literal[
    "API_KEY",
    "AWS_IAM",
    "AMAZON_COGNITO_USER_POOLS",
    "OPENID_CONNECT",
    "AWS_LAMBDA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "API_KEY",
        "AWS_IAM",
        "AMAZON_COGNITO_USER_POOLS",
        "OPENID_CONNECT",
        "AWS_LAMBDA",
    )
)


def serialize_json(value: AuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> AuthenticationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthenticationType value: {data!r}")
    return cast(AuthenticationType, data)
