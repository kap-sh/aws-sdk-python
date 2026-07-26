"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobWarmStartType``."""

from typing import Literal, TypeAlias, cast

HyperParameterTuningJobWarmStartType: TypeAlias = Literal[
    "IdenticalDataAndAlgorithm",
    "TransferLearning",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobWarmStartType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobWarmStartType:
    return cast(HyperParameterTuningJobWarmStartType, data)
