"""Generated from Smithy shape ``com.amazonaws.personalize#TrainingMode``."""

from typing import Literal, TypeAlias, cast

TrainingMode: TypeAlias = Literal[
    "FULL",
    "UPDATE",
    "AUTOTRAIN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingMode:
    return cast(TrainingMode, data)
