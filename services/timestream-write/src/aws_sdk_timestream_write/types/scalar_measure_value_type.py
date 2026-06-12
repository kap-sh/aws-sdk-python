"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ScalarMeasureValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

ScalarMeasureValueType: TypeAlias = Literal[
    "DOUBLE",
    "BIGINT",
    "BOOLEAN",
    "VARCHAR",
    "TIMESTAMP",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOUBLE",
        "BIGINT",
        "BOOLEAN",
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
