"""Generated from Smithy shape ``com.amazonaws.sagemaker#CapacitySizeType``."""

from typing import Literal, TypeAlias, cast

CapacitySizeType: TypeAlias = Literal[
    "INSTANCE_COUNT",
    "CAPACITY_PERCENT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacitySizeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacitySizeType:
    return cast(CapacitySizeType, data)
