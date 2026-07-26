"""Generated from Smithy shape ``com.amazonaws.identitystore#UserStatus``."""

from typing import Literal, TypeAlias, cast

UserStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserStatus:
    return cast(UserStatus, data)
