"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TablePreparationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

TablePreparationMode: TypeAlias = Literal[
    "do-nothing",
    "truncate",
    "drop-tables-on-target",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "do-nothing",
        "truncate",
        "drop-tables-on-target",
    )
)


def serialize_aws_json_1_1(value: TablePreparationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TablePreparationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TablePreparationMode value: {data!r}")
    return cast(TablePreparationMode, data)
