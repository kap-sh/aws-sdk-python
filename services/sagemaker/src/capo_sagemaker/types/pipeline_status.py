"""Generated from Smithy shape ``com.amazonaws.sagemaker#PipelineStatus``."""

from typing import Literal, TypeAlias, cast

PipelineStatus: TypeAlias = Literal[
    "Active",
    "Deleting",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PipelineStatus:
    return cast(PipelineStatus, data)
