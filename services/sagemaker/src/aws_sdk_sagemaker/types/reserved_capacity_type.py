"""Generated from Smithy shape ``com.amazonaws.sagemaker#ReservedCapacityType``."""

from typing import Literal, TypeAlias, cast

ReservedCapacityType: TypeAlias = Literal[
    "UltraServer",
    "Instance",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReservedCapacityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReservedCapacityType:
    return cast(ReservedCapacityType, data)
