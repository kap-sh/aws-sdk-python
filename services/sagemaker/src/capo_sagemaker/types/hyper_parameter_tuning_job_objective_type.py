"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobObjectiveType``."""

from typing import Literal, TypeAlias, cast

HyperParameterTuningJobObjectiveType: TypeAlias = Literal[
    "Maximize",
    "Minimize",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobObjectiveType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobObjectiveType:
    return cast(HyperParameterTuningJobObjectiveType, data)
