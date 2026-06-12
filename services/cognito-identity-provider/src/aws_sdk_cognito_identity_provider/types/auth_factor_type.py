"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthFactorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

AuthFactorType: TypeAlias = Literal[
    "PASSWORD",
    "EMAIL_OTP",
    "SMS_OTP",
    "WEB_AUTHN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSWORD",
        "EMAIL_OTP",
        "SMS_OTP",
        "WEB_AUTHN",
    )
)


def serialize_aws_json_1_1(value: AuthFactorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthFactorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthFactorType value: {data!r}")
    return cast(AuthFactorType, data)
