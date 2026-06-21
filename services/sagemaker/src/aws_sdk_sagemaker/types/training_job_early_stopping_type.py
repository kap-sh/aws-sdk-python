"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobEarlyStoppingType``."""

from typing import Literal, TypeAlias, cast

TrainingJobEarlyStoppingType: TypeAlias = Literal[
    "Off",
    "Auto",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingJobEarlyStoppingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingJobEarlyStoppingType:
    return cast(TrainingJobEarlyStoppingType, data)
