"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardSortBy``."""

from typing import Literal, TypeAlias, cast

ModelCardSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardSortBy:
    return cast(ModelCardSortBy, data)
