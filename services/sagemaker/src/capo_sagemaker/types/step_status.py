"""Generated from Smithy shape ``com.amazonaws.sagemaker#StepStatus``."""

from typing import Literal, TypeAlias, cast

StepStatus: TypeAlias = Literal[
    "Starting",
    "Executing",
    "Stopping",
    "Stopped",
    "Failed",
    "Succeeded",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StepStatus:
    return cast(StepStatus, data)
