"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SqlServerAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

SqlServerAuthenticationMethod: TypeAlias = Literal[
    "password",
    "kerberos",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "password",
        "kerberos",
    )
)


def serialize_aws_json_1_1(value: SqlServerAuthenticationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SqlServerAuthenticationMethod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SqlServerAuthenticationMethod value: {data!r}"
        )
    return cast(SqlServerAuthenticationMethod, data)
