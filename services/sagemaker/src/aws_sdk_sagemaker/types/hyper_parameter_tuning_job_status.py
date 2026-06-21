"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobStatus``."""

from typing import Literal, TypeAlias, cast

HyperParameterTuningJobStatus: TypeAlias = Literal[
    "Completed",
    "InProgress",
    "Failed",
    "Stopped",
    "Stopping",
    "Deleting",
    "DeleteFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HyperParameterTuningJobStatus:
    return cast(HyperParameterTuningJobStatus, data)
