"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceExperimentStatus``."""

from typing import Literal, TypeAlias, cast

InferenceExperimentStatus: TypeAlias = Literal[
    "Creating",
    "Created",
    "Updating",
    "Running",
    "Starting",
    "Stopping",
    "Completed",
    "Cancelled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceExperimentStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceExperimentStatus:
    return cast(InferenceExperimentStatus, data)
