"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolMfaType``."""

from typing import Literal, TypeAlias, cast

UserPoolMfaType: TypeAlias = Literal[
    "OFF",
    "ON",
    "OPTIONAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolMfaType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserPoolMfaType:
    return cast(UserPoolMfaType, data)
