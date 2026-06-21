"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProblemType``."""

from typing import Literal, TypeAlias, cast

ProblemType: TypeAlias = Literal[
    "BinaryClassification",
    "MulticlassClassification",
    "Regression",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProblemType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProblemType:
    return cast(ProblemType, data)
