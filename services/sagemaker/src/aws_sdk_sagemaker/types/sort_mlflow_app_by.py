"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortMlflowAppBy``."""

from typing import Literal, TypeAlias, cast

SortMlflowAppBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SortMlflowAppBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortMlflowAppBy:
    return cast(SortMlflowAppBy, data)
