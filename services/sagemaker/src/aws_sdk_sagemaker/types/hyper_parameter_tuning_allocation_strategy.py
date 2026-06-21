"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningAllocationStrategy``."""

from typing import Literal, TypeAlias, cast

HyperParameterTuningAllocationStrategy: TypeAlias = Literal["Prioritized",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningAllocationStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningAllocationStrategy:
    return cast(HyperParameterTuningAllocationStrategy, data)
