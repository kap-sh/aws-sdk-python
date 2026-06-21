"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrialComponentPrimaryStatus``."""

from typing import Literal, TypeAlias, cast

TrialComponentPrimaryStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrialComponentPrimaryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrialComponentPrimaryStatus:
    return cast(TrialComponentPrimaryStatus, data)
