"""Generated from Smithy shape ``com.amazonaws.timestreamquery#ScalarMeasureValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_query.errors import DeserializationError

ScalarMeasureValueType: TypeAlias = Literal[
    "BIGINT",
    "BOOLEAN",
    "DOUBLE",
    "VARCHAR",
    "TIMESTAMP",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BIGINT",
        "BOOLEAN",
        "DOUBLE",
        "VARCHAR",
        "TIMESTAMP",
    )
)


def serialize_aws_json_1_0(value: ScalarMeasureValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScalarMeasureValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ScalarMeasureValueType value: {data!r}")
    return cast(ScalarMeasureValueType, data)
