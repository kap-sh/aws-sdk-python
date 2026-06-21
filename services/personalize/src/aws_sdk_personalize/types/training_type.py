"""Generated from Smithy shape ``com.amazonaws.personalize#TrainingType``."""

from typing import Literal, TypeAlias, cast

TrainingType: TypeAlias = Literal[
    "AUTOMATIC",
    "MANUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingType:
    return cast(TrainingType, data)
