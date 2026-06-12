"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#RedisAuthTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

RedisAuthTypeValue: TypeAlias = Literal[
    "none",
    "auth-role",
    "auth-token",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "auth-role",
        "auth-token",
    )
)


def serialize_aws_json_1_1(value: RedisAuthTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RedisAuthTypeValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RedisAuthTypeValue value: {data!r}")
    return cast(RedisAuthTypeValue, data)
