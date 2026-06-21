"""Generated from Smithy shape ``com.amazonaws.workmail#UserRole``."""

from typing import Literal, TypeAlias, cast

UserRole: TypeAlias = Literal[
    "USER",
    "RESOURCE",
    "SYSTEM_USER",
    "REMOTE_USER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserRole) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserRole:
    return cast(UserRole, data)
