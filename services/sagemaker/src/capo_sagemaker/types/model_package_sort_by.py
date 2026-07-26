"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageSortBy``."""

from typing import Literal, TypeAlias, cast

ModelPackageSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageSortBy:
    return cast(ModelPackageSortBy, data)
