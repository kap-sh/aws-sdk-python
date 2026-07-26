"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLJobObjectiveType``."""

from typing import Literal, TypeAlias, cast

AutoMLJobObjectiveType: TypeAlias = Literal[
    "Maximize",
    "Minimize",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoMLJobObjectiveType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLJobObjectiveType:
    return cast(AutoMLJobObjectiveType, data)
