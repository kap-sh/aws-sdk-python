"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#VersionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

VersionStatus: TypeAlias = Literal[
    "UP_TO_DATE",
    "OUTDATED",
    "UNSUPPORTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UP_TO_DATE",
        "OUTDATED",
        "UNSUPPORTED",
    )
)


def serialize_aws_json_1_1(value: VersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VersionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VersionStatus value: {data!r}")
    return cast(VersionStatus, data)
