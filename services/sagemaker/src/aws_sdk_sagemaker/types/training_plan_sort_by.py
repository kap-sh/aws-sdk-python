"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanSortBy``."""

from typing import Literal, TypeAlias, cast

TrainingPlanSortBy: TypeAlias = Literal[
    "TrainingPlanName",
    "StartTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingPlanSortBy:
    return cast(TrainingPlanSortBy, data)
