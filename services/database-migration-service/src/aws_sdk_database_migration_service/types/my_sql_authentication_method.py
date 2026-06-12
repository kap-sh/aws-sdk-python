"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#MySQLAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

MySQLAuthenticationMethod: TypeAlias = Literal[
    "password",
    "iam",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "password",
        "iam",
    )
)


def serialize_aws_json_1_1(value: MySQLAuthenticationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MySQLAuthenticationMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MySQLAuthenticationMethod value: {data!r}")
    return cast(MySQLAuthenticationMethod, data)
