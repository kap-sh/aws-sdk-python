"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_firehose.errors import DeserializationError

DatabaseType: TypeAlias = Literal[
    "MySQL",
    "PostgreSQL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MySQL",
        "PostgreSQL",
    )
)


def serialize_aws_json_1_1(value: DatabaseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatabaseType value: {data!r}")
    return cast(DatabaseType, data)
