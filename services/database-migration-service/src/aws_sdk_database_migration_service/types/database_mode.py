"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DatabaseMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

DatabaseMode: TypeAlias = Literal[
    "default",
    "babelfish",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "babelfish",
    )
)


def serialize_aws_json_1_1(value: DatabaseMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseMode value: {data!r}")
    return cast(DatabaseMode, data)
