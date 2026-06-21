"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingPlanFilterName``."""

from typing import Literal, TypeAlias, cast

TrainingPlanFilterName: TypeAlias = Literal["Status",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingPlanFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingPlanFilterName:
    return cast(TrainingPlanFilterName, data)
