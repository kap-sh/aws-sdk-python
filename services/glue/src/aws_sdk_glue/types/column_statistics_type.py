"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ColumnStatisticsType: TypeAlias = Literal[
    "BOOLEAN",
    "DATE",
    "DECIMAL",
    "DOUBLE",
    "LONG",
    "STRING",
    "BINARY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BOOLEAN",
        "DATE",
        "DECIMAL",
        "DOUBLE",
        "LONG",
        "STRING",
        "BINARY",
    )
)


def serialize_aws_json_1_1(value: ColumnStatisticsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ColumnStatisticsType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ColumnStatisticsType value: {data!r}")
    return cast(ColumnStatisticsType, data)
