"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MeasureValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_timestream_write.errors import DeserializationError

MeasureValueType: TypeAlias = Literal[
    "DOUBLE",
    "BIGINT",
    "VARCHAR",
    "BOOLEAN",
    "TIMESTAMP",
    "MULTI",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOUBLE",
        "BIGINT",
        "VARCHAR",
        "BOOLEAN",
        "TIMESTAMP",
        "MULTI",
    )
)


def serialize_aws_json_1_0(value: MeasureValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MeasureValueType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MeasureValueType value: {data!r}")
    return cast(MeasureValueType, data)
