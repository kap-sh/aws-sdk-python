"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#AdjustmentType``."""

from typing import Literal, TypeAlias, cast

AdjustmentType: TypeAlias = Literal[
    "ChangeInCapacity",
    "PercentChangeInCapacity",
    "ExactCapacity",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdjustmentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdjustmentType:
    return cast(AdjustmentType, data)
