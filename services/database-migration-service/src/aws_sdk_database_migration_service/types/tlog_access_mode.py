"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#TlogAccessMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

TlogAccessMode: TypeAlias = Literal[
    "BackupOnly",
    "PreferBackup",
    "PreferTlog",
    "TlogOnly",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BackupOnly",
        "PreferBackup",
        "PreferTlog",
        "TlogOnly",
    )
)


def serialize_aws_json_1_1(value: TlogAccessMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TlogAccessMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TlogAccessMode value: {data!r}")
    return cast(TlogAccessMode, data)
