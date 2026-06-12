"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#NestingLevelValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

NestingLevelValue: TypeAlias = Literal[
    "none",
    "one",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "none",
        "one",
    )
)


def serialize_aws_json_1_1(value: NestingLevelValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NestingLevelValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NestingLevelValue value: {data!r}")
    return cast(NestingLevelValue, data)
