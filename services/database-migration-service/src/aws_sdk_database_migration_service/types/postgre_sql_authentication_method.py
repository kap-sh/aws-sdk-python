"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PostgreSQLAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

PostgreSQLAuthenticationMethod: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: PostgreSQLAuthenticationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PostgreSQLAuthenticationMethod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PostgreSQLAuthenticationMethod value: {data!r}"
        )
    return cast(PostgreSQLAuthenticationMethod, data)
