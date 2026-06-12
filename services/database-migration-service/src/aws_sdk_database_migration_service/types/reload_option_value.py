"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReloadOptionValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

ReloadOptionValue: TypeAlias = Literal[
    "data-reload",
    "validate-only",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "data-reload",
        "validate-only",
    )
)


def serialize_aws_json_1_1(value: ReloadOptionValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReloadOptionValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReloadOptionValue value: {data!r}")
    return cast(ReloadOptionValue, data)
