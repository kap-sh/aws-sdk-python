"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#LongVarcharMappingType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

LongVarcharMappingType: TypeAlias = Literal[
    "wstring",
    "clob",
    "nclob",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "wstring",
        "clob",
        "nclob",
    )
)


def serialize_aws_json_1_1(value: LongVarcharMappingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LongVarcharMappingType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LongVarcharMappingType value: {data!r}")
    return cast(LongVarcharMappingType, data)
