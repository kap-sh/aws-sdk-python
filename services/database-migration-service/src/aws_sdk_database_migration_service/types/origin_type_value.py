"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#OriginTypeValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

OriginTypeValue: TypeAlias = Literal[
    "SOURCE",
    "TARGET",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOURCE",
        "TARGET",
    )
)


def serialize_aws_json_1_1(value: OriginTypeValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OriginTypeValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OriginTypeValue value: {data!r}")
    return cast(OriginTypeValue, data)
