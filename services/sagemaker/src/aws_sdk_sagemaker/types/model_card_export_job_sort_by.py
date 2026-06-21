"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCardExportJobSortBy``."""

from typing import Literal, TypeAlias, cast

"""Attribute by which to sort returned export jobs."""
ModelCardExportJobSortBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCardExportJobSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCardExportJobSortBy:
    return cast(ModelCardExportJobSortBy, data)
