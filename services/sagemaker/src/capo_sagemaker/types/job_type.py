"""Generated from Smithy shape ``com.amazonaws.sagemaker#JobType``."""

from typing import Literal, TypeAlias, cast

JobType: TypeAlias = Literal[
    "TRAINING",
    "INFERENCE",
    "NOTEBOOK_KERNEL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobType:
    return cast(JobType, data)
