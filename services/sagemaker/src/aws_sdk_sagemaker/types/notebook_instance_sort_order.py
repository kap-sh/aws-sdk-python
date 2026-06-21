"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceSortOrder``."""

from typing import Literal, TypeAlias, cast

NotebookInstanceSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookInstanceSortOrder:
    return cast(NotebookInstanceSortOrder, data)
