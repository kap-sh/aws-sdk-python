"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserStatusType``."""

from typing import Literal, TypeAlias, cast

UserStatusType: TypeAlias = Literal[
    "UNCONFIRMED",
    "CONFIRMED",
    "ARCHIVED",
    "COMPROMISED",
    "UNKNOWN",
    "RESET_REQUIRED",
    "FORCE_CHANGE_PASSWORD",
    "EXTERNAL_PROVIDER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserStatusType:
    return cast(UserStatusType, data)
