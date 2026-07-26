"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#ScalarMeasureValueType``."""

from typing import Literal, TypeAlias, cast

ScalarMeasureValueType: TypeAlias = Literal[
    "DOUBLE",
    "BIGINT",
    "BOOLEAN",
    "VARCHAR",
    "TIMESTAMP",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ScalarMeasureValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ScalarMeasureValueType:
    return cast(ScalarMeasureValueType, data)
