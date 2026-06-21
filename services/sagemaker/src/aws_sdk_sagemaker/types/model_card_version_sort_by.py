"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardVersionSortBy``."""

from typing import Literal, TypeAlias, cast

ModelCardVersionSortBy: TypeAlias = Literal["Version",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardVersionSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardVersionSortBy:
    return cast(ModelCardVersionSortBy, data)
