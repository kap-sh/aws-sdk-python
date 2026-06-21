"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanSortOrder``."""

from typing import Literal, TypeAlias, cast

TrainingPlanSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingPlanSortOrder:
    return cast(TrainingPlanSortOrder, data)
