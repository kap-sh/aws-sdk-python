"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobSortByOptions``."""

from typing import Literal, TypeAlias, cast

TrainingJobSortByOptions: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
    "FinalObjectiveMetricValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingJobSortByOptions) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingJobSortByOptions:
    return cast(TrainingJobSortByOptions, data)
