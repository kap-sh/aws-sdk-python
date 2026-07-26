"""Generated from Smithy shape ``com.amazonaws.applicationautoscaling#ScalingActivityStatusCode``."""

from typing import Literal, TypeAlias, cast

ScalingActivityStatusCode: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Successful",
    "Overridden",
    "Unfulfilled",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingActivityStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingActivityStatusCode:
    return cast(ScalingActivityStatusCode, data)
