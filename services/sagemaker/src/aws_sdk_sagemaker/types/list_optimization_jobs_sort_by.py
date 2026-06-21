"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListOptimizationJobsSortBy``."""

from typing import Literal, TypeAlias, cast

ListOptimizationJobsSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOptimizationJobsSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ListOptimizationJobsSortBy:
    return cast(ListOptimizationJobsSortBy, data)
