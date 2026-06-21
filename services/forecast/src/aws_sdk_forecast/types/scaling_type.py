"""Generated from Smithy shape ``com.amazonaws.forecast#ScalingType``."""

from typing import Literal, TypeAlias, cast

ScalingType: TypeAlias = Literal[
    "Auto",
    "Linear",
    "Logarithmic",
    "ReverseLogarithmic",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ScalingType:
    return cast(ScalingType, data)
