"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

EventType: TypeAlias = Literal[
    "SignIn",
    "SignUp",
    "ForgotPassword",
    "PasswordChange",
    "ResendCode",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SignIn",
        "SignUp",
        "ForgotPassword",
        "PasswordChange",
        "ResendCode",
    )
)


def serialize_aws_json_1_1(value: EventType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventType value: {data!r}")
    return cast(EventType, data)
