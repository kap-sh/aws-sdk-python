"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlgorithmSortBy``."""

from typing import Literal, TypeAlias, cast

AlgorithmSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlgorithmSortBy:
    return cast(AlgorithmSortBy, data)
