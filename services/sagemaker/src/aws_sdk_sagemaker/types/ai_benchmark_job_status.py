"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIBenchmarkJobStatus``."""

from typing import Literal, TypeAlias, cast

AIBenchmarkJobStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
    "Stopping",
    "Stopped",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIBenchmarkJobStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AIBenchmarkJobStatus:
    return cast(AIBenchmarkJobStatus, data)
