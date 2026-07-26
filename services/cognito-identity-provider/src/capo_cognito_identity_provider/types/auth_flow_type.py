"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthFlowType``."""

from typing import Literal, TypeAlias, cast

AuthFlowType: TypeAlias = Literal[
    "USER_SRP_AUTH",
    "REFRESH_TOKEN_AUTH",
    "REFRESH_TOKEN",
    "CUSTOM_AUTH",
    "ADMIN_NO_SRP_AUTH",
    "USER_PASSWORD_AUTH",
    "ADMIN_USER_PASSWORD_AUTH",
    "USER_AUTH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthFlowType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthFlowType:
    return cast(AuthFlowType, data)
