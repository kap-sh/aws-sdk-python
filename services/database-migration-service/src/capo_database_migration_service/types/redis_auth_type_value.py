"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RedisAuthTypeValue``."""

from typing import Literal, TypeAlias, cast

RedisAuthTypeValue: TypeAlias = Literal[
    "none",
    "auth-role",
    "auth-token",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedisAuthTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedisAuthTypeValue:
    return cast(RedisAuthTypeValue, data)
