"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AuthTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

AuthTypeValue: TypeAlias = Literal[
    "no",
    "password",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "no",
        "password",
    )
)


def serialize_aws_json_1_1(value: AuthTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthTypeValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AuthTypeValue value: {data!r}")
    return cast(AuthTypeValue, data)
