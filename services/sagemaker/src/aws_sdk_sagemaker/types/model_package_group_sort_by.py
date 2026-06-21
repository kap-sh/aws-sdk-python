"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageGroupSortBy``."""

from typing import Literal, TypeAlias, cast

ModelPackageGroupSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelPackageGroupSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageGroupSortBy:
    return cast(ModelPackageGroupSortBy, data)
