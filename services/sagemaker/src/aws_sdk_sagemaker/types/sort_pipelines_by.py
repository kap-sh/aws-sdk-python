"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortPipelinesBy``."""

from typing import Literal, TypeAlias, cast

SortPipelinesBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortPipelinesBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortPipelinesBy:
    return cast(SortPipelinesBy, data)
