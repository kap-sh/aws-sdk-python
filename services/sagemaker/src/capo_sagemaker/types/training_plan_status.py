"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanStatus``."""

from typing import Literal, TypeAlias, cast

TrainingPlanStatus: TypeAlias = Literal[
    "Pending",
    "Active",
    "Scheduled",
    "Expired",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingPlanStatus:
    return cast(TrainingPlanStatus, data)
