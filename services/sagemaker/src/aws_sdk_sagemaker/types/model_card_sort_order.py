"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardSortOrder``."""

from typing import Literal, TypeAlias, cast

ModelCardSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardSortOrder:
    return cast(ModelCardSortOrder, data)
