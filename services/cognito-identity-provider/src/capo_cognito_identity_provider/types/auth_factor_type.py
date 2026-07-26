"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthFactorType``."""

from typing import Literal, TypeAlias, cast

AuthFactorType: TypeAlias = Literal[
    "PASSWORD",
    "EMAIL_OTP",
    "SMS_OTP",
    "WEB_AUTHN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthFactorType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthFactorType:
    return cast(AuthFactorType, data)
