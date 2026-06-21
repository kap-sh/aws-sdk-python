"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortPipelineExecutionsBy``."""

from typing import Literal, TypeAlias, cast

SortPipelineExecutionsBy: TypeAlias = Literal[
    "CreationTime",
    "PipelineExecutionArn",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortPipelineExecutionsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortPipelineExecutionsBy:
    return cast(SortPipelineExecutionsBy, data)
