"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ChallengeNameType``."""

from typing import Literal, TypeAlias, cast

ChallengeNameType: TypeAlias = Literal[
    "SMS_MFA",
    "EMAIL_OTP",
    "SOFTWARE_TOKEN_MFA",
    "SELECT_MFA_TYPE",
    "MFA_SETUP",
    "PASSWORD_VERIFIER",
    "CUSTOM_CHALLENGE",
    "SELECT_CHALLENGE",
    "DEVICE_SRP_AUTH",
    "DEVICE_PASSWORD_VERIFIER",
    "ADMIN_NO_SRP_AUTH",
    "NEW_PASSWORD_REQUIRED",
    "SMS_OTP",
    "PASSWORD",
    "WEB_AUTHN",
    "PASSWORD_SRP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChallengeNameType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChallengeNameType:
    return cast(ChallengeNameType, data)
