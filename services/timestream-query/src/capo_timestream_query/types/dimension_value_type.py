"""Generated from Smithy shape ``com.amazonaws.timestreamquery#DimensionValueType``."""

from typing import Literal, TypeAlias, cast

DimensionValueType: TypeAlias = Literal["VARCHAR",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DimensionValueType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DimensionValueType:
    return cast(DimensionValueType, data)
