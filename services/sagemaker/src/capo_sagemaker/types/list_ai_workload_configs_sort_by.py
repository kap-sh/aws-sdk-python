"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListAIWorkloadConfigsSortBy``."""

from typing import Literal, TypeAlias, cast

ListAIWorkloadConfigsSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAIWorkloadConfigsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListAIWorkloadConfigsSortBy:
    return cast(ListAIWorkloadConfigsSortBy, data)
