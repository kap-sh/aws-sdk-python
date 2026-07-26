"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportJobSortOrder``."""

from typing import Literal, TypeAlias, cast

ModelCardExportJobSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardExportJobSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardExportJobSortOrder:
    return cast(ModelCardExportJobSortOrder, data)
