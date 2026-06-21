"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmStatus``."""

from typing import Literal, TypeAlias, cast

AlgorithmStatus: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Completed",
    "Failed",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlgorithmStatus:
    return cast(AlgorithmStatus, data)
