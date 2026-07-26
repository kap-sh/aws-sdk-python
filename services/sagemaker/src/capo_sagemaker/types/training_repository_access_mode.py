"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingRepositoryAccessMode``."""

from typing import Literal, TypeAlias, cast

TrainingRepositoryAccessMode: TypeAlias = Literal[
    "Platform",
    "Vpc",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingRepositoryAccessMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TrainingRepositoryAccessMode:
    return cast(TrainingRepositoryAccessMode, data)
