"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ReleaseStatusValues``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

ReleaseStatusValues: TypeAlias = Literal[
    "beta",
    "prod",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "beta",
        "prod",
    )
)


def serialize_aws_json_1_1(value: ReleaseStatusValues) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReleaseStatusValues:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ReleaseStatusValues value: {data!r}")
    return cast(ReleaseStatusValues, data)
