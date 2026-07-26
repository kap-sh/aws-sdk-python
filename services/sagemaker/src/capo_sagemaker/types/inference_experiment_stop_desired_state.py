"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentStopDesiredState``."""

from typing import Literal, TypeAlias, cast

InferenceExperimentStopDesiredState: TypeAlias = Literal[
    "Completed",
    "Cancelled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceExperimentStopDesiredState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceExperimentStopDesiredState:
    return cast(InferenceExperimentStopDesiredState, data)
