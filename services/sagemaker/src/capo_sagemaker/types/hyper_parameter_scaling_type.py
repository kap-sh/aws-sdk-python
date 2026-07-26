"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterScalingType``."""

from typing import Literal, TypeAlias, cast

HyperParameterScalingType: TypeAlias = Literal[
    "Auto",
    "Linear",
    "Logarithmic",
    "ReverseLogarithmic",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterScalingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterScalingType:
    return cast(HyperParameterScalingType, data)
