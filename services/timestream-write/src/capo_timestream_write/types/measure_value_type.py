"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#MeasureValueType``."""

from typing import Literal, TypeAlias, cast

MeasureValueType: TypeAlias = Literal[
    "DOUBLE",
    "BIGINT",
    "VARCHAR",
    "BOOLEAN",
    "TIMESTAMP",
    "MULTI",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MeasureValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MeasureValueType:
    return cast(MeasureValueType, data)
