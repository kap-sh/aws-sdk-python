"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScalarType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

ScalarType: TypeAlias = Literal[
    "VARCHAR",
    "BOOLEAN",
    "BIGINT",
    "DOUBLE",
    "TIMESTAMP",
    "DATE",
    "TIME",
    "INTERVAL_DAY_TO_SECOND",
    "INTERVAL_YEAR_TO_MONTH",
    "UNKNOWN",
    "INTEGER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VARCHAR",
        "BOOLEAN",
        "BIGINT",
        "DOUBLE",
        "TIMESTAMP",
        "DATE",
        "TIME",
        "INTERVAL_DAY_TO_SECOND",
        "INTERVAL_YEAR_TO_MONTH",
        "UNKNOWN",
        "INTEGER",
    )
)


def serialize_aws_json_1_0(value: ScalarType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScalarType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalarType value: {data!r}")
    return cast(ScalarType, data)
