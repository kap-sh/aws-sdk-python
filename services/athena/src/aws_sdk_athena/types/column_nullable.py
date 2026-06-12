"""Generated from Smithy shape ``com.amazonaws.athena#ColumnNullable``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

ColumnNullable: TypeAlias = Literal[
    "NOT_NULL",
    "NULLABLE",
    "UNKNOWN",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_NULL",
        "NULLABLE",
        "UNKNOWN",
    )
)


def serialize_aws_json_1_1(value: ColumnNullable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ColumnNullable:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnNullable value: {data!r}")
    return cast(ColumnNullable, data)
