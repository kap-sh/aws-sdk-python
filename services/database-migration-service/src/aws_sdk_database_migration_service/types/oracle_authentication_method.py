"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#OracleAuthenticationMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

OracleAuthenticationMethod: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: OracleAuthenticationMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OracleAuthenticationMethod:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OracleAuthenticationMethod value: {data!r}"
        )
    return cast(OracleAuthenticationMethod, data)
