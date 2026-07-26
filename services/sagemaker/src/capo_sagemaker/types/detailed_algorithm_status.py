"""Generated from Smithy shape ``com.amazonaws.sagemaker#DetailedAlgorithmStatus``."""

from typing import Literal, TypeAlias, cast

DetailedAlgorithmStatus: TypeAlias = Literal[
    "NotStarted",
    "InProgress",
    "Completed",
    "Failed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetailedAlgorithmStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetailedAlgorithmStatus:
    return cast(DetailedAlgorithmStatus, data)
