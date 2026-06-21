"""Generated from Smithy shape ``com.amazonaws.timestreamquery#MeasureValueType``."""

from typing import Literal, TypeAlias, cast

MeasureValueType: TypeAlias = Literal[
    "BIGINT",
    "BOOLEAN",
    "DOUBLE",
    "VARCHAR",
    "MULTI",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MeasureValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MeasureValueType:
    return cast(MeasureValueType, data)
