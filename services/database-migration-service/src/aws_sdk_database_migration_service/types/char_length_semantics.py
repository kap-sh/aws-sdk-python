"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CharLengthSemantics``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_database_migration_service.errors import DeserializationError

CharLengthSemantics: TypeAlias = Literal[
    "default",
    "char",
    "byte",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "default",
        "char",
        "byte",
    )
)


def serialize_aws_json_1_1(value: CharLengthSemantics) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CharLengthSemantics:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CharLengthSemantics value: {data!r}")
    return cast(CharLengthSemantics, data)
