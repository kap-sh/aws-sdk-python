"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolTierType``."""

from typing import Literal, TypeAlias, cast

UserPoolTierType: TypeAlias = Literal[
    "LITE",
    "ESSENTIALS",
    "PLUS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolTierType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserPoolTierType:
    return cast(UserPoolTierType, data)
